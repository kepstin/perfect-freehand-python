# MIT License
#
# Copyright (c) 2022 Calvin Walton
# Copyright (c) 2021 Stephen Ruiz

"""Support types for Python type hints."""

from typing import TypedDict
from typing import Tuple


class InputPoint(TypedDict, total=False):
    """The structure of a point dict that can be used as input to
    :func:`.get_stroke_points`

    This ``TypedDict`` class is only used for typechecking; you can use an
    ordinary ``dict`` with the keys described here.
    """

    x: float
    """The x coordinate of the point."""

    y: float
    """The y coordinate of the point."""

    pressure: float
    """The stylus pressure associated with the point. Optional."""


class StrokePoint(TypedDict):
    """The structure of a point dict that is the output from
    :func:`.get_stroke_points`

    This ``TypedDict`` class is only used for typechecking; the returned
    points are accessed in the same way as a normal dict.
    """

    point: Tuple[float, float]
    """The x/y position of the point."""

    pressure: float
    """The stylus pressure associated with the point, or synthesized."""

    distance: float
    """The linear distance from the previous point to this point."""

    vector: Tuple[float, float]
    """The motion vector from the previous point to this point."""

    running_length: float
    """The sum of all distances up to this point."""
