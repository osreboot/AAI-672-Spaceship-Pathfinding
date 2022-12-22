import numpy as np


class Path:

    def __init__(self, length):
        self.length = length
        self.values = []
        for i in range(length):
            self.values.append([
                np.random.uniform(0.0, 10.0),  # Timing of maneuver
                np.random.uniform(0.0, 360.0)  # Direction of burn
            ])

    def crossover(self, other):
        indices = np.random.randint(0, len(self.values), int(self.length / 2))
        for i in indices:
            if np.random.uniform(0.0, 1.0) < 0.5:
                self.values[i] = other.values[i]
            if np.random.uniform(0.0, 1.0) < 0.2:
                self.values[i] = [
                    np.random.uniform(0.0, 10.0),  # Timing of maneuver
                    np.random.uniform(0.0, 360.0)  # Direction of burn
                ]
