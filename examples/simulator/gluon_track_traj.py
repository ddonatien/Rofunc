"""
Tracking the trajectory by Gluon
============================================================

This example runs a Tai Chi demo trajectory by using Gluon.
"""
import os
import numpy as np
from isaacgym import gymutil
import rofunc as rf

args = gymutil.parse_arguments()
args.use_gpu_pipeline = False

traj = np.load(os.path.join(rf.file.get_rofunc_path(), 'data/taichi_1l.npy'))
# print(traj)
traj = traj*0.2
rf.lqt.plot_3d_uni(traj, ori=False)l;

gluonsim = rf.sim.GluonSim(args)
gluonsim.run_traj(traj)

