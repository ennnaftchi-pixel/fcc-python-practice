"""
FreeCodeCamp Python Practice
Exercise: User Settings Manager

Concepts practiced:
- Dictionary operations (CRUD)
- Functions and return values
- Input normalization
- Defensive programming

Description:
This exercise simulates managing user settings using a dictionary.
It supports adding, updating, deleting, and viewing settings
with validation and user-friendly feedback.

Status: Learning exercise
"""

test_settings = {
    "theme": "light",
    "volume": "medium"
}


def add_setting(settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()

    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"


def delete_setting(settings, key):
    key = key.lower()

    if key not in settings:
        return "Setting not found!"

    del settings[key]
    return f"Setting '{key}' deleted successfully!"


def view_settings(settings):
    if not settings:
        return "No settings available."

    output = "Current User Settings:\n"
    for key, value in settings.items():
        output += f"{key.capitalize()}: {value}\n"

    return output


if __name__ == "__main__":
    settings = test_settings.copy()

    print(view_settings(settings))
    print(add_setting(settings, ("language", "English")))
    print(update_setting(settings, ("volume", "High")))
    print(delete_setting(settings, "theme"))
    print(view_settings(settings))
