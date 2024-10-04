from dataclasses import dataclass

@dataclass
class Point:
	x: int
	y: int

@dataclass
class Coordinates:
	mylist: list[Point]


