from geometry import


class Velocity:
    _mps_to_fps = 3.281

    def __init__(self, fps=None, mps=None):
        self._fps = 0.0

        if mps is not None:
            self._fps = mps * self._mps_to_fps
        elif fps is not None:
            self._fps = fps
        else:
            raise ValueError("Velocity units cannot be determined")

    def _get(self, factor):
        return self._fps / factor

    @property
    def mps(self):
        return self._get(self._mps_to_fps)

    @property
    def fps(self):
        return self._fps

    def __add__(self, other):
        if isinstance(other, Velocity):
            return Velocity(self._fps + other._fps)
        raise TypeError(f"Cannot add Velocity to {type(other)}")

    def __sub__(self, other):
        if isinstance(other, Velocity):
            return Velocity(self._fps - other._fps)
        raise TypeError(f"Cannot subtract Velocity by {type(other)}")

    def __truediv__(self, other):
        if isinstance(other, Time):
            return Length(ft=self.fps / other.seconds)
        elif isinstance(other, Velocity):
            return self.fps / other.fps
        raise TypeError(f"Cannot divide Velocity by {type(other)}")

    #TODO: eq and str