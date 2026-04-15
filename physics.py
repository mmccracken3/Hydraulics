import utils
from geometry import Length, Time, Area, Volume


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

    def __mul__(self, other):
        if isinstance(other, Time):
            return Length(ft=self.fps * other.seconds)
        raise TypeError(f"Cannot multiply Velocity by {type(other)}")

    def __truediv__(self, other):
        if isinstance(other, Velocity):
            return self.fps / other.fps
        raise TypeError(f"Cannot divide Velocity by {type(other)}")

    def __rtruediv__(self, other):
        if isinstance(other, Length):
            return Time(seconds=other.ft / self.fps)
        raise TypeError(f"Cannot divide {type(other)} by Velocity")

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Velocity):
            return False
        return utils.are_close_enough(self, other)

    def __str__(self):
        return f'{self.fps} fps'


class Flow:
    _gps_to_cfs = 7.48052
    _gpm_to_cfs = _gps_to_cfs * 60
    _gpd_to_cfs = _gpm_to_cfs * 60 * 24
    _mgd_to_cfs = _gpd_to_cfs / 1e6
    _cms_to_cfs = 1 / (3.281) ** 3

    def __init__(self, mgd=None, gpd=None, gpm=None, gps=None, cfs=None, cms=None):
        self._cfs = 0.0

        if mgd is not None:
            self._cfs = mgd * self._mgd_to_cfs
        elif gpd is not None:
            self._cfs = gpd * self._gpd_to_cfs
        elif gpm is not None:
            self._cfs = gpm * self._gpm_to_cfs
        elif gps is not None:
            self._cfs = gps * self._gps_to_cfs
        elif cfs is not None:
            self._cfs = cfs
        elif cms is not None:
            self._cfs = cms * self._cms_to_cfs
        else:
            raise TypeError('Flow units cannot be determined.')

    def _get(self, factor):
        return self._cfs / factor

    @property
    def mgd(self):
        return self._get(self._mgd_to_cfs)

    @property
    def gpd(self):
        return self._get(self._gpd_to_cfs)

    @property
    def gpm(self):
        return self._get(self._gpm_to_cfs)

    @property
    def gps(self):
        return self._get(self._gps_to_cfs)

    @property
    def cfs(self):
        return self._cfs

    @property
    def cms(self):
        return self._get(self._cms_to_cfs)

    def __add__(self, other):
        if isinstance(other, Flow):
            return Flow(self._cfs + other._cfs)
        raise TypeError(f"Cannot add Flow to {type(other)}")

    def __sub__(self, other):
        if isinstance(other, Flow):
            return Flow(self._cfs - other._cfs)
        raise TypeError(f"Cannot subtract Flow from {type(other)}")

    def __mul__(self, other):
        if isinstance(other, Time):
            return Volume(cf=self.cfs * other.seconds)
        raise TypeError(f"Cannot multiply Flow by {type(other)}")

    def __truediv__(self, other):
        if isinstance(other, Area):
            return Velocity(fps=self.cfs / other.sf)
        elif isinstance(other, Velocity):
            return Area(sf=self.cfs / other.fps)
        elif isinstance(other, Flow):
            return self.cfs / other.cfs
        raise TypeError(f"Cannot divide Flow by {type(other)}")

    def __rtruediv__(self, other):
        if isinstance(other, Volume):
            return Time(seconds=other.cf / self.cfs)
        raise TypeError(f"Cannot divide {type(other)} by Flow")

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Flow):
            return False
        return utils.are_close_enough(self.cfs, other.cfs)

    def __str__(self):
        return (f'{self.cfs} cfs\n'
                f'{self.mgd} mgd\n'
                f'{self.gpm} gpm\n')
