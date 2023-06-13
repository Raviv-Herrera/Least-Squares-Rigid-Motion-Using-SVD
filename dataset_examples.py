import numpy as np


class Torus:

    def __init__(self, num_of_points: int):

        self._num_of_points = num_of_points

        u = np.linspace(0, np.pi, num_of_points)
        v = np.linspace(0, 2 * np.pi, num_of_points)

        shift = np.random.randint(0, 6)

        self._x = np.outer(shift + np.sin(u), np.sin(v))
        self._y = np.outer(shift + np.sin(u), np.cos(v))
        self._z = np.outer(np.cos(u), np.ones_like(v))

        self._torus = np.zeros((3, num_of_points * num_of_points))
        self._torus[0, :] = self._x.ravel()
        self._torus[1, :] = self._y.ravel()
        self._torus[2, :] = self._z.ravel()

    def create_shifted_torus(self):

        t2 = Torus(self._num_of_points)
        t2._x = self._x + 3
        t2._y = self._y + 3
        t2._z = self._z + 5

        return t2

    @property
    def torus(self): return self._torus

    @property
    def x(self): return self._x

    @property
    def y(self): return self._y

    @property
    def z(self): return self._z
