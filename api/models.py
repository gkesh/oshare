from pydantic.dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    username: str


@dataclass
class OshareResponse:
    message: str
