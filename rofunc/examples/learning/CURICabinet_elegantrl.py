"""
CURICabinet (ElegantRL)
===========================

Open drawers with a humanoid CURI robot, trained by ElegantRL
"""

import argparse
import isaacgym

from elegantrl.train.run import train_and_evaluate

from rofunc.utils.logger.beauty_logger import beauty_print
from rofunc.data.models import model_zoo
from rofunc.lfd.rl.utils.elegantrl_utils import setup


def train(custom_args):
    beauty_print("Start training")

    env, args = setup(custom_args)

    # start training
    train_and_evaluate(args)


def eval(custom_args, ckpt_path=None):
    # TODO: add support for eval mode
    beauty_print("Start evaluating")

    env, args = setup(custom_args, eval_mode=True)

    # load checkpoint
    if ckpt_path is None:
        ckpt_path = model_zoo(name="CURICabinetPPO_right_arm.pt")
    agent.load(ckpt_path)

    # evaluate the agent
    trainer.eval()


if __name__ == '__main__':
    gpu_id = 1
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", type=str, default="CURICabinet")
    parser.add_argument("--agent", type=str, default="sac")
    parser.add_argument("--sim_device", type=str, default="cuda:{}".format(gpu_id))
    parser.add_argument("--rl_device", type=str, default="cuda:{}".format(gpu_id))
    parser.add_argument("--graphics_device_id", type=int, default=gpu_id)
    parser.add_argument("--headless", type=str, default="False")
    parser.add_argument("--test", action="store_true", help="turn to test mode while adding this argument")
    custom_args = parser.parse_args()

    if not custom_args.test:
        train(custom_args)
    else:
        # TODO: add support for eval mode
        folder = 'CURICabinetSAC_22-11-27_18-38-53-296354'
        ckpt_path = "/home/ubuntu/Github/Knowledge-Universe/Robotics/Roadmap-for-robot-science/rofunc/examples/learning/runs/{}/checkpoints/best_agent.pt".format(
            folder)
        eval(custom_args, ckpt_path=ckpt_path)
