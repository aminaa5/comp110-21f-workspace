"""Practice with dictionaries."""

__author__ = "730398576"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Funtion to invert keys and values."""
    y = {}
    for key in x:
        if x[key] in y:
            raise KeyError("STOP! The keys are the same. That's no good!")
    for key in x:
        y[x[key]] = key    
    return y


def favorite_color(x: dict[str, str]) -> str:
    """Spits out the most frequent favorite color!"""
    y: dict[str, int] = {}
    for key in x:
        colors = x[key]
        if colors in y:
            y[colors] += 1
        else:
            y[colors] = 1
    i: int = 0
    words: str = ""
    for key in y:
        times = y[key]
        if times > i:
            i = times
            words = key
    return words


def count(x: list[str]) -> dict[str, int]:
    """Funtion to determine the frequency of each key."""
    y: dict[str, int] = {}
    for item in x:
        if item in y:
            y[item] += 1
        else:
            y[item] = 1
    return y