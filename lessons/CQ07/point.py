"""CQ 07."""

from __future__ import annotations

__author__ = 730555961


class Point:
    """Defining a new class."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """My constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutates original point by a factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Creates new point and mutates that point by a factor."""
        new_point: Point = Point(self.x, self.y)
        new_point.x = self.x * factor
        new_point.y = self.y * factor
        return new_point

    def __str__(self) -> str:
        """Print out the Point in a readable format."""
        point_info: str = f"x: {self.x}; y: {self.y}"
        return point_info
    
    def __mul__(self, factor: int | float) -> Point:
        """Magic method overloader for multiplication of Point."""
        new_point: Point = Point(self.x, self.y)
        new_point.x = self.x * factor
        new_point.y = self.y * factor
        return new_point
    
    def __add__(self, factor: int | float) -> Point:
        """Magic method overloader for addition to Point."""
        new_point: Point = Point(self.x, self.y)
        new_point.x = self.x + factor
        new_point.y = self.y + factor
        return new_point