class SpaceAge:

    EARTH_YEAR = 365.25
    DAY_SEC = 86_400

    YEAR_DUR = {
        'earth': EARTH_YEAR,    # in days
        'mercury': 0.2408467 * EARTH_YEAR,
        'venus': 0.61519726 * EARTH_YEAR,
        'mars':  1.8808158 * EARTH_YEAR,
        'jupiter': 11.862615 * EARTH_YEAR,
        'saturn': 29.447498 * EARTH_YEAR,
        'uranus':  84.016846 * EARTH_YEAR,
        'neptune':  164.79132 * EARTH_YEAR,
    }

    def __init__(self, seconds):
        # d, s  = divmod(seconds, __class__.DAY_SEC)
        self.day = seconds / __class__.DAY_SEC
        self.sec = seconds

    def on_earth(self):
        return round(self.day / __class__.YEAR_DUR['earth'], 2)

    def on_mercury(self):
        return round(self.day / __class__.YEAR_DUR['mercury'], 2)

    def on_venus(self):
        return round(self.day / __class__.YEAR_DUR['venus'], 2)

    def on_mars(self):
        return round(self.day / __class__.YEAR_DUR['mars'], 2)

    def on_jupiter(self):
        return round(self.day / __class__.YEAR_DUR['jupiter'], 2)

    def on_saturn(self):
        return round(self.day / __class__.YEAR_DUR['saturn'], 2)

    def on_uranus(self):
        return round(self.day / __class__.YEAR_DUR['uranus'], 2)

    def on_neptune(self):
        return round(self.day / __class__.YEAR_DUR['neptune'], 2)
