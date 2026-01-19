"""
FreeCodeCamp Python Practice
Exercise: Musical Instrument Class

Concepts practiced:
- Classes and objects
- Constructors (__init__)
- Instance attributes
- Instance methods

Description:
This exercise demonstrates basic object-oriented programming in Python
by modeling a musical instrument and its behavior.

Status: Learning exercise
"""

class MusicalInstrument:
    def __init__(self, name, instrument_type):
        self.name = name
        self.instrument_type = instrument_type

    def play(self):
        print(f"The {self.name} is fun to play!")

    def get_fact(self):
        return f"The {self.name} is part of the {self.instrument_type} family of instruments."


if __name__ == "__main__":
    instrument_1 = MusicalInstrument("Oboe", "woodwind")
    instrument_2 = MusicalInstrument("Trumpet", "brass")

    instrument_1.play()
    print(instrument_1.get_fact())

    instrument_2.play()
    print(instrument_2.get_fact())
