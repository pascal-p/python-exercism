class ClockParms:
    HOUR_SEC = 3600     # in sec.
    MIN_SEC = 60        # in sec.
    PREC = ['minute', 'second']
    DAY_HOUR = 24       # num. of hour in a day
    DAY_MIN  = 24 * 60  # num. of min. in a day
    DAY_SEC = 86_400    # 1 day in sec.

class Clock:

    def __init__(self, hour, minute, second=0, precision='minute'):
        self.sec = __class__._to_s(hour, minute, second)
        assert precision in ClockParms.PREC
        self.prec = precision

    def __repr__(self):
        if self.prec == 'minute':
            (hour, minute) = __class__._to_hm(self.sec)
            return f"{hour:02}:{minute:02}"
        elif self.prec == 'second':
            (hour, minute, sec) = __class__._to_hms(self.sec)
            return f"{hour:02}:{minute:02}:{sec:02}"
        #
        raise(ValueError(f"Unknown precision {self.prec} / allowed values: {ClockParms.PREC}"))

    def __eq__(self, other):
        return self.prec == other.prec and self.sec == other.sec

    def __add__(self, minutes, seconds=0):
        if self.prec == 'second':
             minute, seconds = divmod(seconds, ClockParms.MIN_SEC)
             self.sec += seconds
             minutes += minute

        self.sec = __class__.add_min(minutes, self.sec)
        return self

    def add(self, minutes, seconds=0):
        return self.__add__(minutes, seconds)

    def __sub__(self, minutes, seconds=0):
        # careful to a - b when b > a / across midnight
        if self.prec == 'second':
            minute, seconds = divmod(seconds, ClockParms.MIN_SEC)
            self.sec += seconds
            minutes += minute

        if self.sec < minutes * ClockParms.MIN_SEC:
            days, minutes = divmod(minutes, ClockParms.DAY_MIN)
            self.sec += (days + 1) * ClockParms.DAY_SEC

        minutes %= ClockParms.DAY_MIN
        self.sec -= minutes * ClockParms.MIN_SEC
        if self.sec < 0:
            self.sec %= ClockParms.HOUR_SEC

        return self

    def sub(self, minutes, seconds=0):
        return self.__sub__(minutes, seconds)
    #
    # Internal Helpers
    #
    @staticmethod
    def add_min(minutes, sec):
        sec += minutes * ClockParms.MIN_SEC
        if sec < 0:
            sec %= ClockParms.HOUR_SEC
        return sec

    @staticmethod
    def _to_s(hour:int, minute:int, second:int=0) -> int :
        hh = 0
        if minute >= ClockParms.MIN_SEC or minute <= 0:
            hh, minute = divmod(minute, ClockParms.MIN_SEC)
        #
        hour += hh
        hour %= ClockParms.DAY_HOUR
        rsec = hour * ClockParms.HOUR_SEC + minute * ClockParms.MIN_SEC
        assert rsec >= 0
        #
        if second > rsec:
            days, second = divmod(second, ClockParms.DAY_SEC)
            rsec += (days + 1) * ClockParms.DAY_SEC
        rsec += second
        #
        return rsec % ClockParms.DAY_SEC

    @staticmethod
    def _to_hm(sec:int):
        hour, rsec = divmod(sec, ClockParms.HOUR_SEC)
        hour %= ClockParms.DAY_HOUR
        minute, _ = divmod(rsec, ClockParms.MIN_SEC)
        return (hour, minute)

    @staticmethod
    def _to_hms(sec:int):
        hour, rsec = divmod(sec, ClockParms.HOUR_SEC)
        hour %= ClockParms.DAY_HOUR
        minute, rsec = divmod(rsec, ClockParms.MIN_SEC)
        return (hour, minute, rsec)
