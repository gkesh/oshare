from enum import IntEnum, auto
from pydantic.dataclasses import dataclass


class Gender(IntEnum):
    MALE: auto()
    FEMALE: auto()

@dataclass
class User:
    first_name: str
    last_name: str
    username: str
    gender: Gender
    age: int


@dataclass
class OshareResponse:
    message: str
