from dataclasses import dataclass, field
import sqlite3 as sql

@dataclass
class C:
	a: int
	b: int = 0

@dataclass
class D:
	mylist: list[int] = field(default_factory=list)
