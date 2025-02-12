from typing import Tuple

import numpy as np
import pbdlib as pbd
from numpy import ndarray
from scipy.linalg import block_diag

import rofunc as rf
from rofunc.learning.ml.tpgmm.tpgmm import TPGMM
from rofunc.utils.logger.beauty_logger import beauty_print


class TPGMR(TPGMM):
    def __init__(self, demos_x, nb_states: int = 4, reg: float = 1e-3, horizon=150, plot=False):
        """
        Task-parameterized Gaussian Mixture Regression (TP-GMR)
        :param demos_x: demo displacement
        :param nb_states: number of states in the HMM
        :param reg: regularization term
        :param horizon: horizon of the reproduced trajectory
        :param plot: whether to plot the result
        """
        super().__init__(demos_x, nb_states=nb_states, reg=reg, horizon=horizon, plot=plot)
        self.gmr = rf.learning.gmr.GMR(self.demos_x, self.demos_dx, self.demos_xdx, nb_states=nb_states, reg=reg, plot=False)

    def gmm_learning(self):
        # Learn the time-dependent GMR from demonstration
        t = np.linspace(0, 10, self.demos_x[0].shape[0])
        demos = [np.hstack([t[:, None], d]) for d in self.demos_xdx_augm]
        self.gmr.demos = demos
        model = self.gmr.gmm_learning()
        mu_gmr, sigma_gmr = self.gmr.estimate(model, t[:, None], dim_in=slice(0, 1),
                                              dim_out=slice(1, 4 * len(self.demos_x[0]) + 1))
        model = pbd.GMM(mu=mu_gmr, sigma=sigma_gmr)
        return model

    def _reproduce(self, model: pbd.HMM, prod: pbd.GMM, show_demo_idx: int, start_xdx: np.ndarray) -> np.ndarray:
        """
        Reproduce the specific demo_idx from the learned model
        :param model: learned model
        :param prod: result of PoE
        :param show_demo_idx: index of the specific demo to be reproduced
        :return:
        """
        lqr = pbd.PoGLQR(nb_dim=len(self.demos_x[0][0]), dt=0.01, horizon=self.demos_xdx[show_demo_idx].shape[0])

        mvn = pbd.MVN()
        mvn.mu = np.concatenate([i for i in prod.mu])
        mvn._sigma = block_diag(*[i for i in prod.sigma])

        lqr.mvn_xi = mvn
        lqr.mvn_u = -4
        lqr.x0 = start_xdx

        xi = lqr.seq_xi
        if self.plot:
            if len(self.demos_x[0][0]) == 2:
                rf.tpgmm.generate_plot(xi, prod, self.demos_x, show_demo_idx)
            elif len(self.demos_x[0][0]) > 2:
                rf.tpgmm.generate_plot_3d(xi, prod, self.demos_x, show_demo_idx, scale=0.1)
            else:
                raise Exception('Dimension is less than 2, cannot plot')
        return xi

    def fit(self):
        beauty_print('Learning the trajectory representation from demonstration via TP-GMR')

        model = self.gmm_learning()
        return model

    def reproduce(self, model, show_demo_idx):
        beauty_print('reproduce {}-th demo from learned representation'.format(show_demo_idx), type='info')

        prod = self.poe(model, show_demo_idx)
        traj = self._reproduce(model, prod, show_demo_idx, self.demos_xdx[show_demo_idx][0])
        return traj

    def generate(self, model: pbd.HMM, ref_demo_idx: int, task_params: dict) -> np.ndarray:
        beauty_print('generate new demo from learned representation', type='info')

        task_params_A_b = self.get_task_params_A_b(task_params)

        prod = self.poe(model, ref_demo_idx, task_params_A_b)
        traj = self._reproduce(model, prod, ref_demo_idx, task_params['start_xdx'])
        return traj


class TPGMRBi(TPGMR):
    def __init__(self, demos_left_x, demos_right_x, horizon=150, plot=False):
        self.demos_left_x = demos_left_x
        self.demos_right_x = demos_right_x
        self.plot = plot

        self.repr_l = TPGMR(demos_left_x)
        self.repr_r = TPGMR(demos_right_x)

    def fit(self):
        beauty_print('Learning the trajectory representation from demonstration via TP-GMR')

        model_l = self.repr_l.gmm_learning()
        model_r = self.repr_r.gmm_learning()
        return model_l, model_r

    def reproduce(self, model_l, model_r, show_demo_idx):
        beauty_print('reproduce {}-th demo from learned representation'.format(show_demo_idx), type='info')

        prod_l = self.repr_l.poe(model_l, show_demo_idx)
        prod_r = self.repr_r.poe(model_r, show_demo_idx)
        traj_l = self.repr_l._reproduce(model_l, prod_l, show_demo_idx, self.repr_l.demos_xdx[show_demo_idx][0])
        traj_r = self.repr_r._reproduce(model_r, prod_r, show_demo_idx, self.repr_r.demos_xdx[show_demo_idx][0])

        if self.plot:
            nb_dim = int(traj_l.shape[1] / 2)
            data_lst = [traj_l[:, :nb_dim], traj_r[:, :nb_dim]]
            rf.visualab.traj_plot(data_lst)
        return traj_l, traj_r

    def generate(self, model_l: pbd.HMM, model_r: pbd.HMM, ref_demo_idx: int, task_params: dict) -> \
            Tuple[ndarray, ndarray]:
        beauty_print('generate new demo from learned representation', type='info')

        task_params_A_b_l = self.repr_l.get_task_params_A_b(task_params['Left'])
        task_params_A_b_r = self.repr_r.get_task_params_A_b(task_params['Right'])

        prod_l = self.repr_l.poe(model_l, ref_demo_idx, task_params_A_b_l)
        prod_r = self.repr_r.poe(model_r, ref_demo_idx, task_params_A_b_r)
        traj_l = self.repr_l._reproduce(model_l, prod_l, ref_demo_idx, task_params['Left']['start_xdx'])
        traj_r = self.repr_r._reproduce(model_r, prod_r, ref_demo_idx, task_params['Right']['start_xdx'])

        if self.plot:
            nb_dim = int(traj_l.shape[1] / 2)
            data_lst = [traj_l[:, :nb_dim], traj_r[:, :nb_dim]]
            rf.visualab.traj_plot(data_lst)
        return traj_l, traj_r
