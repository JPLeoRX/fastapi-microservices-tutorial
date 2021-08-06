from injectable import injectable, autowired, Autowired
from library_message_protocol import Ping
from .utils_id import UtilsId
from .utils_time import UtilsTime


@injectable
class UtilsPing:
    @autowired
    def __init__(self, utils_id: Autowired(UtilsId), utils_time: Autowired(UtilsTime)):
        self.utils_id = utils_id
        self.utils_time = utils_time

    def generate_ping(self) -> Ping:
        t = self.utils_time.get_current_timestamp_ms()
        t_str = self.utils_time.format_timestamp_ms(t)

        return Ping(
            self.utils_id.generate_uuid(),
            True,
            t,
            t_str
        )
