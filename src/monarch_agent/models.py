from dataclasses import asdict, dataclass, field
from typing import Optional
import hashlib
import json


@dataclass(frozen=True)
class AvailabilityResult:
    check_in: str
    check_out: str
    status: str
    room_name: Optional[str] = None
    nightly_rate: Optional[str] = None
    total_rate: Optional[str] = None
    cancellation_policy: Optional[str] = None
    occupancy: Optional[str] = None
    notes: Optional[str] = None
    raw_matches: list[str] = field(default_factory=list)

    def fingerprint(self) -> str:
        payload = json.dumps(asdict(self), sort_keys=True)
        return hashlib.sha256(payload.encode()).hexdigest()
