from fastapi import APIRouter
from library_message_protocol import Ping
from library_utils import UtilsPing


router_ping = APIRouter()
utils_ping = UtilsPing()


@router_ping.get("/ping", response_model=Ping)
def ping() -> Ping:
    return utils_ping.generate_ping()
