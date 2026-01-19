"""
Planet Class Exercise
This file contains a Planet class implementation as part of FreeCodeCamp Python practice.
Demonstrates object-oriented programming, validation, __str__, and instance methods.
"""

class Planet:
    def __init__(self, name, planet_type, star):
        # Type validation
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError("name, planet type, and star must be strings")

        # Empty string validation
        if name == "" or planet_type == "" or star == "":
            raise ValueError("name, planet_type, and star must be non-empty strings")

        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f"{self.name} is orbiting around {self.star}...."

    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"


if __name__ == "__main__":
    # Create instances
    planet_1 = Planet("Earth", "Terrestrial", "Sun")
    planet_2 = Planet("Jupiter", "Gas Giant", "Sun")
    planet_3 = Planet("Kepler-22b", "Exoplanet", "Kepler-22")

    # Print info
    print(planet_1)
    print(planet_2)
    print(planet_3)

    # Call orbit method
    print(planet_1.orbit())
    print(planet_2.orbit())
    print(planet_3.orbit())
