from datetime import datetime
import time
from injectable import injectable


@injectable
class UtilsTime:
    def get_current_timestamp_ms(self) -> int:
        return int(time.time_ns() // 1000000)

    def format_timestamp_ms(self, timestamp_ms: int) -> str:
        return datetime.utcfromtimestamp(timestamp_ms / 1000).strftime('%d.%m.%Y %H:%M:%S')
