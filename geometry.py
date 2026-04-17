import utils


class Length:
    _inch_to_ft = 1 / 12
    _mile_to_ft = 5280
    _m_to_ft = 3.281


    def __init__(self, ft=None, inch=None, mile=None, m=None):
        self._ft = 0.0

        if inch is not None:
            self._ft = inch * self._inch_to_ft
        elif mile is not None:
            self._ft = mile * self._mile_to_ft
        elif m is not None:
            self._ft = m * self._m_to_ft
        elif ft is not None:
            self._ft = ft
        else:
            raise ValueError("Length units cannot be determined.")

    def _get(self, factor):
        return self._ft / factor

    # def _set(self, value, factor):
    #     self._ft = value * factor

    @property
    def ft(self):
        return self._ft

    # @ft.setter
    # def ft(self, value):
    #     self._ft = value

    @property
    def inch(self):
        return self._get(self._inch_to_ft)

    # @inch.setter
    # def inch(self, value):
    #     self._set(value, self._inch_to_ft)

    @property
    def mile(self):
        return self._get(self._mile_to_ft)

    # @mile.setter
    # def mile(self, value):
    #     self._set(value, self._mile_to_ft)

    @property
    def m(self):
        return self._get(self._m_to_ft)

    # @m.setter
    # def m(self, value):
    #     self._set(value, self._m_to_ft)

    def __add__(self, other):
        if isinstance(other, Length):
            return Length(ft=self.ft + other.ft)

        raise ValueError(f'Length cannot be added by {type(other)}.')

    def __sub__(self, other):
        if isinstance(other, Length):
            return Length(ft=self.ft - other.ft)

        raise TypeError(f'Length cannot be subtracted by {type(other)}.')

    def __mul__(self, other):
        if isinstance(other, Length):
            return Area(sf=self.ft * other.ft)
        elif isinstance(other, Area):
            return Volume(cf=other.sf * self.ft)
        elif isinstance(other, int) or isinstance(other, float):
            return Length(ft=self.ft * other)
        else:
            raise TypeError(f'Length cannot be multiplied by {type(other)}.')

    # def __rmul__(self, other):
    #     if isinstance(other, Length):
    #         return Length(ft=self.ft * other.ft)
    #     elif isinstance(other, Area):
    #         return Volume(other.sf * self.ft)
    #     elif isinstance(other, int) or isinstance(other, float):
    #         return Length(ft=self.ft * other)
    #     else:
    #         raise TypeError(f'Length cannot be multiplied by {type(other)}.')

    def __truediv__(self, other):
        if isinstance(other, Length):
            return self.ft / other.ft
        elif isinstance(other, int) or isinstance(other, float):
            return Length(ft=self.ft / other)
        else:
            raise TypeError(f'Length cannot be divided by {type(other)}.')

    # def __rtruediv__(self, other):
    #     if isinstance(other, Length):
    #         return float(self.ft) / float(other.ft)
    #     elif isinstance(other, Area):
    #         return Length(ft=other.sf / self.ft)
    #     elif isinstance(other, Volume):
    #         return Area(sf=other.cf / self.ft)
    #     else:
    #         raise TypeError(f'{type(other)} cannot be divided by Length.')

    def __pow__(self, other):
        if other == 2:
            return Area(sf=self.ft ** 2)
        elif other == 3:
            return Volume(cf=self.ft ** 3)
        else:
            raise TypeError(f'Length cannot be raised to {type(other)}.')

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Length):
            return False

        return utils.are_close_enough(self.ft, other.ft)

    def __str__(self):
        return (f'{self.ft:.5g} ft\n'
                f'{self.inch:.5g} inch')


class Area:
    _in2_to_sf = 1 / 144
    _mile2_to_sf = 27878400
    _ac_to_sf = 43560
    _m2_to_sf = 3.281 ** 2

    def __init__(self, sf=None, inch2=None, mile2=None, ac=None, m2=None):
        self._sf = 0.0

        if inch2 is not None:
            self._sf = inch2 * self._in2_to_sf
        elif mile2 is not None:
            self._sf = mile2 * self._mile2_to_sf
        elif ac is not None:
            self._sf = ac * self._ac_to_sf
        elif sf is not None:
            self._sf = sf
        elif m2 is not None:
            self._sf = m2 * self._m2_to_sf
        else:
            raise ValueError("Area units cannot be determined.")

    def _get(self, factor):
        return self._sf / factor

    # def _set(self, value, factor):
    #     self._sf = value * factor

    @property
    def sf(self):
        return self._sf

    # @sf.setter
    # def sf(self, value):
    #     self._sf = value

    @property
    def inch2(self):
        return self._get(self._in2_to_sf)

    # @inch2.setter
    # def inch2(self, value):
    #     self._set(value, self._in2_to_sf)

    @property
    def mile2(self):
        return self._get(self._mile2_to_sf)

    # @mile2.setter
    # def mile2(self, value):
    #     self._set(value, self._mile2_to_sf)

    @property
    def ac(self):
        return self._get(self._ac_to_sf)

    # @ac.setter
    # def ac(self, value):
    #     self._set(value, self._ac_to_sf)

    @property
    def m2(self):
        return self._get(self._m2_to_sf)

    # @m2.setter
    # def m2(self, value):
    #     self._set(value, self._m2_to_sf)

    def __add__(self, other):
        if isinstance(other, Area):
            return Area(self._sf + other._sf)

        raise ValueError(f'Area cannot be added by {type(other)}.')

    def __sub__(self, other):
        if isinstance(other, Area):
            return Area(self._sf - other._sf)

        raise ValueError(f'Area cannot be subtracted by {type(other)}.')

    def __mul__(self, other):
        if isinstance(other, Length):
            return Volume(cf=self.sf * other.ft)
        elif isinstance(other, int) or isinstance(other, float):
            return Area(sf=self.sf * other)
        else:
            raise TypeError(f'Area cannot be multiplied by {type(other)}.')

    # def __rmul__(self, other):
    #     if isinstance(other, Length):
    #         return Volume(cf=self.sf * other.ft)
    #     elif isinstance(other, int) or isinstance(other, float):
    #         return Area(sf=self.sf * other)
    #     else:
    #         raise TypeError(f'Area cannot be multiplied by {type(other)}.')

    def __truediv__(self, other):
        if isinstance(other, Length):
            return Length(ft=self.sf / other.ft)
        elif isinstance(other, Area):
            return self.sf / other.sf
        elif isinstance(other, int) or isinstance(other, float):
            return Area(sf=self.sf / other)
        else:
            raise TypeError(f'Area cannot be divided by {type(other)}.')

    # def __rtruediv__(self, other):
    #     if isinstance(other, Volume):
    #         return Length(ft=other.cf / self.sf)
    #     elif isinstance(other, Area):
    #         return other.sf / self.sf
    #     else:
    #         raise TypeError(f'{type(other)} cannot be divided by area.')

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Area):
            return False

        return utils.are_close_enough(self.sf, other.sf)

    def __str__(self):
        return (f'{self.sf:.5g} sf\n'
                f'{self.inch2:.5g} inch2\n')

class Volume:
    _gal_to_cf = 1 / 7.48052
    _m3_to_cf = 3.281 ** 3

    def __init__(self, cf=None, gal=None, m3=None):
        self._cf = 0.0

        if gal is not None:
            self._cf = gal * self._gal_to_cf
        elif m3 is not None:
            self._cf = m3 * self._m3_to_cf
        elif cf is not None:
            self._cf = cf
        else:
            raise ValueError("Volume units cannot be determined.")

    def _get(self, factor):
        return self._cf / factor

    # def _set(self, value, factor):
    #     self._cf = value * factor

    @property
    def cf(self):
        return self._cf

    # @cf.setter
    # def cf(self, value):
    #     self._cf = value

    @property
    def gal(self):
        return self._get(self._gal_to_cf)

    # @gal.setter
    # def gal(self, value):
    #     self._set(value, self._gal_to_cf)

    @property
    def m3(self):
        return self._get(self._m3_to_cf)

    # @m3.setter
    # def m3(self, value):
    #     self._set(value, self._m3_to_cf)

    def __add__(self, other):
        if isinstance(other, Volume):
            return Volume(cf=self.cf + other.cf)

        raise TypeError(f'Volume cannot be added by {type(other)}.')

    def __sub__(self, other):
        if isinstance(other, Volume):
            return Volume(cf=self.cf - other.cf)

        raise TypeError(f'Volume cannot be subtracted by {type(other)}.')

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Volume(cf=self.cf * other)

        raise TypeError(f'Volume cannot be multiplied by {type(other)}.')

    # def __rmul__(self, other):
    #     if isinstance(other, int) or isinstance(other, float):
    #         return Volume(cf=self.cf * other)
    #
    #     raise TypeError(f'Volume cannot be multiplied by {type(other)}.')

    def __truediv__(self, other):
        if isinstance(other, Volume):
            return self.cf / other.cf
        if isinstance(other, Area):
            return Length(ft=self.cf / other.sf)
        if isinstance(other, Length):
            return Area(sf=self.cf / other.ft)
        if isinstance(other, int) or isinstance(other, float):
            return Volume(cf=self.cf / other)
        else:
            raise TypeError(f'Volume cannot be divided by {type(other)}.')

    # def __rtruediv__(self, other):
    #     if isinstance(other, Volume):
    #         return other.cf / self.cf
    #
    #     raise TypeError(f'{type(other)} cannot be divided by Volume.')

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Volume):
            return False

        return utils.are_close_enough(self.cf, other.cf)

    def __str__(self):
        return (f'{self.cf:.5g} cf\n'
                f'{self.gal:.5g} gal\n')


class Time:
    _min_to_sec = 60
    _hour_to_sec = 3600
    _day_to_sec = 86400

    def __init__(self, days=None, hours=None, minutes=None, seconds=None):
        self._seconds = 0.0

        if days is not None:
            self._seconds = days * self._day_to_sec
        elif hours is not None:
            self._seconds = hours * self._hour_to_sec
        elif minutes is not None:
            self._seconds = minutes * self._min_to_sec
        elif seconds is not None:
            self._seconds = seconds
        else:
            raise TypeError(f'Time units cannot be determined.')

    def _get(self, factor):
        return self._seconds / factor

    @property
    def seconds(self):
        return self._seconds

    @property
    def minutes(self):
        return self._get(self._min_to_sec)

    @property
    def hours(self):
        return self._get(self._hour_to_sec)

    @property
    def days(self):
        return self._get(self._day_to_sec)

    def __add__(self, other):
        if isinstance(other, Time):
            return Time(seconds=self.seconds + other.seconds)
        raise TypeError(f'Time cannot be added by {type(other)}.')

    def __sub__(self, other):
        if isinstance(other, Time):
            return Time(seconds=self.seconds - other.seconds)
        raise TypeError(f'Time cannot be subtracted by {type(other)}.')

#TODO: multiply to get velocity, flow?

    def __truediv__(self, other):
        if isinstance(other, Time):
            return self.seconds / other.seconds
        elif isinstance(other, int) or isinstance(other, float):
            return Time(seconds=self.seconds / other)
        raise TypeError(f'Time cannot be divided by {type(other)}.')

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Time):
            return False

        return utils.are_close_enough(self.seconds, other.seconds)

    def __str__(self):
        return (f'{self.seconds:.5g} seconds\n'
                f'{self.minutes:.5g} minutes\n'
                f'{self.hours:.5g} hours\n'
                f'{self.days:.5g} days\n')
