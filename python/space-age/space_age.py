class SpaceAge:
    planets = {'mercury': 0.2408467,
               'venus': 0.61519726,
               'earth': 1,
               'mars': 1.8808158,
               'jupiter': 11.862615,
               'saturn': 29.447498,
               'uranus': 84.016846,
               'neptune': 164.79132,
               }

    EARTH_YEAR_DAYS = 364.25
    EARTH_YEAR_SECONDS = 31557600

    years = 0
    seconds = 0

    def __init__(self, seconds):
        self.seconds = seconds
        self.years = seconds / self.EARTH_YEAR_SECONDS

    def on_mercury(self):
        return round(self.years / self.planets['mercury'], 2)

    def on_venus(self):
        return round(self.years / self.planets['venus'], 2)

    def on_earth(self):
        return round(self.years, 2)

    def on_mars(self):
        return round(self.years / self.planets['mars'], 2)

    def on_jupiter(self):
        return round(self.years / self.planets['jupiter'], 2)

    def on_saturn(self):
        return round(self.years / self.planets['saturn'], 2)

    def on_uranus(self):
        return round(self.years / self.planets['uranus'], 2)

    def on_neptune(self):
        return round(self.years / self.planets['neptune'], 2)
