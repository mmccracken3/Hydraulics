

class Length:
    _inch_to_ft = 1/12
    _mile_to_ft = 1/5280
    _m_to_ft = 1/3.281


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
            raise ValueError("Length value cannot be determined.")

    def _get(self, factor):
        return self._ft * factor

    def _set(self, value, factor):
        self._ft = value * factor

    @property
    def ft(self):
        return self._ft

    @ft.setter
    def ft(self, value):
        self._ft = value

    @property
    def inch(self):
        return self._get(self._inch_to_ft)

    @inch.setter
    def inch(self, value):
        self._set(value, self._inch_to_ft)

    @property
    def mile(self):
        return self._get(self._m_to_ft)

    @mile.setter
    def mile(self, value):
        self._set(value, self._mile_to_ft)

    @property
    def m(self):
        return self._get(self._m_to_ft)

    @m.setter
    def m(self, value):
        self._set(value, self._mile_to_ft)
