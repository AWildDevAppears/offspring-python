
from enum import Enum


class OffspringErrorCodes(Enum):
    NO_FAIL = "NO_FAIL"
    HUB_INVENTORY_FULL = "HUB_INVENTORY_FULL"

class OffspringError():
    def __init__(self, message: str, ref: OffspringErrorCodes) -> None:
        self.message: str = message
        self.ref: OffspringErrorCodes = ref

class OffspringResponse():
    def __init__(
        self,
        failed: bool,
        message: str = "",
        error_ref: OffspringErrorCodes = OffspringErrorCodes.NO_FAIL,
        data: object | None = None
    ) -> None:
        self.failed = failed
        self.message = message
        self.error_ref = error_ref
        self.data = data
