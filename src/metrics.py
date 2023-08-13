from dataclasses import dataclass
import datetime


@dataclass
class Metrics:
    time: datetime.datetime
    cpu_temp: float
    clock_freq: int
