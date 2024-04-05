from dataclasses import dataclass
from datetime import datetime

@dataclass
class Event:
    name: str
    date: datetime
    url: str

@dataclass
class Venue:
    name: str
    capacity: int

@dataclass
class Artist:
    name: str