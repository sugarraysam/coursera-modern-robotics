import numpy as np
import modern_robotics as mr


class Question1:
    def __init__(self, n, theta):
        self.n = n
        self.theta = theta

    def jacobian(self):
        x = self.theta[0, 0]
        y = self.theta[1, 0]
        return np.array([[2 * x, 0], [0, 2 * y]])

    def f(self):
        x = self.theta[0, 0]
        y = self.theta[1, 0]
        return np.array([x ** 2 - 9, y ** 2 - 4]).reshape(2, 1)

    def solve(self):
        for i in range(self.n):
            e = np.zeros((2, 1)) - self.f()
            self.theta = self.theta + np.dot(np.linalg.pinv(self.jacobian()), e)
        return self.theta


class Question2:
    def __init__(self):
        self.Slist = np.array(
            [[0, 0, 1, 0, 0, 0], [0, 0, 1, 0, -1, 0], [0, 0, 1, 0, -2, 0]]
        ).T
        self.M = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [3, 0, 0, 1]]).T
        self.theta0 = np.full(3, 0.7854)
        self.T = np.array(
            [
                [-0.585, -0.811, 0, 0.076],
                [0.811, -0.585, 0, 2.608],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
            ]
        )
        self.eomg = 0.001
        self.ev = 0.0001

    def solve(self):
        return mr.IKinSpace(self.Slist, self.M, self.T, self.theta0, self.eomg, self.ev)


if __name__ == "__main__":
    q1 = Question1(2, np.array([1, 1]).reshape(2, 1))
    print(f"solution q1 [x,y]: {q1.solve()}")

    q2 = Question2()
    sols2, success = q2.solve()
    if success:
        print(sols2)
