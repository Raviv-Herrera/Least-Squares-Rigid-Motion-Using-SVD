import numpy as np
import matplotlib.pyplot as plt
from rigid_body_trans_class import RigidBodyTrans
from loguru import logger
from typing import Any


class Viewer3D:

    @staticmethod
    def plot(shape1: Any, shape2: Any, rbt: RigidBodyTrans) -> None:
        """
        This function plots the 2 shapes
        :param rbt:
        :param shape1:
        :param shape2:
        :return:
        """

        ax = plt.axes(projection='3d')

        ax.set_xlim3d(-15, 10)
        ax.set_ylim3d(-15, 10)
        ax.set_zlim3d(0, 10)

        ax.set_xlabel("X - axis", color='r')
        ax.set_ylabel("Y - axis", color='r')
        ax.set_zlabel("Z - axis", color='r')

        ax.plot_wireframe(shape1.x, shape1.y, shape1.z, color='b')
        ax.plot_wireframe(shape2.x, shape2.y, shape2.z, color='r')
        plt.pause(5)

        shape3 = rbt.R @ rbt.p + rbt.t

        sz = int(len(shape3[0]) ** 0.5)

        ax.plot_wireframe(shape3[0].reshape((sz, sz)),
                          shape3[1].reshape((sz, sz)),
                          shape3[2].reshape((sz, sz)), color='y')

        logger.info(f" Error = {np.sum(np.abs(shape2.torus -shape3))}")
        plt.show()
