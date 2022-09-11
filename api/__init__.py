from typing import Tuple
from quart import Blueprint
from quart_schema import validate_request, validate_response
from api.models import User, OshareResponse


bp_api = Blueprint(
    "bp_api",
    __name__,
    url_prefix="/api/v1"
)

@bp_api.get("/greet")
async def greet_get() -> Tuple[OshareResponse, int]:
    return OshareResponse("Hello there!"), 200

@bp_api.post("/greet")
@validate_request(User)
@validate_response(OshareResponse, 200)
async def greet(data: User) -> Tuple[OshareResponse, int]:
    return OshareResponse(f"Hello there! {data.first_name} {data.last_name}."), 200