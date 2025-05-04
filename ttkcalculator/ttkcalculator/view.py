"""
The view module contains API specifications (i.e. protocols) used
by the KeypadController (see controller module) to facilitate rendering
of the calculator GUI.
"""
from enum import StrEnum
from typing import Protocol, Any


# Indicate what's relevant for other modules to import
__all__ = ['KeyCode', 'Key', 'DisplayView', 'KeypadView']


class KeyCode(StrEnum):
    """ IDs and labels of all calculator keypad keys """
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    ZERO = '0'
    DECIMAL_POINT = '.'
    NEGATE = '±'
    CLEAR = 'C'
    BACKSPACE = '←'
    EQUALS = '='
    PLUS = '+'
    MINUS = '-'
    MULTIPLY = '×'
    DIVIDE = '÷'


class DisplayView(Protocol):
    """
    Interface / protocol to decouple from TKInter dependencies.
    See tkview.TkDisplayView for an actual implementation
    """
    @property
    def tk_variable(self) -> Any:
        """ Property used as adapter between controller and display widget """

    def update(self, text: str) -> None:
        """ Property used as adapter between controller and display widget """

    @property
    def max_items(self) -> int:
        """ Property holding maximal number of items a display can show """


class Key(Protocol):
    """
    Interface / protocol to decouple from TKInter dependencies.
    See tkview.TkKeyButton for an actual implementation
    """

    @property
    def code(self) -> KeyCode:
        """ Property with ID of the actual Key """

    def press(self):
        """ Switches button visualization to 'pressed' state """

    def release(self):
        """ Deactivates the 'pressed' state of a button """


class KeypadView(Protocol):
    """
    Interface / protocol to decouple from TKInter dependencies
    See tkview.TkKeypadView for an actual implementation
    """
    def register(self, key: Key) -> None:
        """ Adds new button widget to this view """

    def press(self, code: KeyCode) -> None:
        """ Switches button identified by its pad_key value into 'pressed' visual state """

    def release_all(self) -> None:
        """ Switches all registered buttons into 'not pressed' visual state """
