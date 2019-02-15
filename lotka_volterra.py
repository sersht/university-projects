import matplotlib.pyplot as plt
import numpy as np


# current_population[0] - preys amount
# current_population[1] - predators amount

class LotkaVolterra:
    def __init__(self, a, b, c, d, dt, initial):
        self.A = a
        self.B = b
        self.C = c
        self.D = d

        self.dt = dt
        self.populations = [initial]

    def _make_step(self):
        return self._runge_kutta()

    def _get_system_values(self, population):
        dx = (self.A - self.B * population[1]) * population[0]
        dy = (self.D * population[0] - self.C) * population[1]
        return (dx, dy)

    def _euler(self):
        population = self.populations[-1]
        dx, dy = self._get_system_values(population)
        return (population[0] + dx * self.dt, population[1] + dy * self.dt)

    def _runge_kutta(self):
        population = self.populations[-1]

        k1 = self._get_system_values(
            population
        )
        k2 = self._get_system_values(
            population + (self.dt / 2 + k1[0], self.dt / 2 + k1[1])
        )
        k3 = self._get_system_values(
            population + (self.dt / 2 + k2[0], self.dt / 2 + k2[1])
        )
        k4 = self._get_system_values(
            population + (self.dt + k3[0], self.dt + k3[1])
        )

        x = population[0] + self.dt * \
            (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        y = population[1] + self.dt * \
            (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6

        return (x, y)

    def generate_populations(self, iterations):
        for i in range(iterations):
            self.populations.append(self._make_step())

    # rewrite on standard getter, setter methods
    def get_populations(self):
        return self.populations


if __name__ == "__main__":
    a = 1.1
    b = 0.4
    c = 0.4
    d = 0.1

    init = (20, 5)
    dt = 10**-3

    lv = LotkaVolterra(a, b, c, d, dt, init)
    lv.generate_populations(100000)
    populs = lv.get_populations()

    x = [dt*i for i in range(len(populs))]
    preys = [x[0] for x in populs]
    preds = [x[1] for x in populs]
    
    plt.plot(x, preys, 'b', x, preds, 'r')

    # plt.xlim(0, 100)
    # plt.ylim(0, 25)

    plt.show()
