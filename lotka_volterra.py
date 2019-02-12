# current_population[0] - preys amount
# current_population[1] - predators amount


class LotkaVolterra:
    def __init__(self, a, b, c, d, dt, initial):
        self.A = a
        self.B = b
        self.C = c
        self.D = d

        self.dt = dt
        self.current_population = initial

    def _make_step(self):
        # Euler's method
        dx = (
            (self.A - self.B * self.current_population[1]) * self.current_population[0])
        dy = (
            (self.D * self.current_population[0] - self.C) * self.current_population[1])

        return (self.current_population[0] + dx * self.dt, self.current_population[1] + dy * self.dt)

    def get_population_dynamic(self, time):
        steps = [self.current_population]
        for i in range(time):
            next_population = self._make_step()
            steps.append(next_population)
            self.current_population = next_population
        return steps


if __name__ == "__main__":
    a = 2 / 3
    b = 0.67
    c = 1.2
    d = 0.8

    init = (10, 4)
    dt = 0.1

    lv = LotkaVolterra(a, b, c, d, dt, init)
    for x in lv.get_population_dynamic(30):
        print(x)
