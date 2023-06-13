import numpy as np
from loguru import logger
from alive_progress import alive_bar


class RigidBodyTrans:

    def __init__(self, p: np.ndarray, q: np.ndarray):
        self._p = p
        self._q = q
        self._R = []
        self._t = []

    def calc_transformation(self) -> None:
        """
        This method calculates the Rotation matrix (R) and the translation vector (t).
        :return:
        """

        if self._p.shape[0] != self._q.shape[0]:
            logger.error("Dimensions Error")
            raise Exception("Dimensions are not equal")

        logger.info("Start calculating R and t ")
        with alive_bar(1) as bar:
            cen_P = np.mean(self._p, axis=1).reshape(-1, 1)
            cen_Q = np.mean(self._q, axis=1).reshape(-1, 1)

            X = self._p - cen_P
            Y = self._q - cen_Q

            S = X @ Y.T

            U, sigma, Vt = np.linalg.svd(S)

            d = np.eye(Vt.T.shape[1])
            d[-1, -1] = np.linalg.det(Vt.T @ U.T)

            self._R = Vt.T @ d @ U.T
            self._t = cen_Q - self._R @ cen_P

            logger.success("Done")
            logger.info(f"R = {self._R} \n\n t = {self._t}")
            bar()

    @property
    def R(self): return self._R

    @property
    def t(self): return self._t

    @property
    def p(self): return self._p

    @property
    def q(self): return self._q
