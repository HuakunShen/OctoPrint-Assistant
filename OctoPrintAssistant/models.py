from django.db import models

# Create your models here.
import enum
from dataclasses import dataclass


@dataclass
class DurationStruct:
    days: int
    hours: int
    minutes: int
    seconds: int

    def is_0(self):
        return self.days + self.hours + self.minutes + self.seconds == 0

# Using enum class create enumerations
class DurationPrecision(enum.IntEnum):
    days = 0
    hours = 1
    minutes = 2
    seconds = 3