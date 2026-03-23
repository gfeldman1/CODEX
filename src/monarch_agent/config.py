import os
from dataclasses import dataclass
from datetime import date, timedelta


@dataclass(frozen=True)
class StayWindow:
    check_in: str
    check_out: str


@dataclass(frozen=True)
class AgentConfig:
    property_url: str
    adults: int
    children: int
    start_month: int
    end_month: int
    min_nights: int
    max_nights: int
    year: int
    target_room_terms: tuple[str, ...]


def _int_env(name: str, default: int) -> int:
    value = os.getenv(name)
    return int(value) if value else default


def _room_terms() -> tuple[str, ...]:
    raw = os.getenv("TARGET_ROOM_TERMS", "3 bedroom penthouse suite,3 bedroom suite,3 bedroom penthouse,3 bedroom villa")
    return tuple(term.strip().lower() for term in raw.split(",") if term.strip())


def load_config() -> AgentConfig:
    today = date.today()
    default_year = today.year if today.month <= 11 else today.year + 1
    return AgentConfig(
        property_url=os.getenv("PROPERTY_URL", "https://www.marriott.com/en-us/hotels/hhhmo-marriotts-monarch-at-sea-pines/overview/"),
        adults=_int_env("ADULTS", 2),
        children=_int_env("CHILDREN", 0),
        start_month=_int_env("START_MONTH", 3),
        end_month=_int_env("END_MONTH", 11),
        min_nights=_int_env("MIN_NIGHTS", 7),
        max_nights=_int_env("MAX_NIGHTS", 7),
        year=_int_env("SEARCH_YEAR", default_year),
        target_room_terms=_room_terms(),
    )


def generate_stay_windows(config: AgentConfig) -> list[StayWindow]:
    windows: list[StayWindow] = []
    current = date(config.year, config.start_month, 1)
    end_boundary = date(config.year, config.end_month + 1, 1) if config.end_month < 12 else date(config.year + 1, 1, 1)

    while current < end_boundary:
        for nights in range(config.min_nights, config.max_nights + 1):
            check_out = current + timedelta(days=nights)
            if check_out <= end_boundary:
                windows.append(StayWindow(check_in=current.isoformat(), check_out=check_out.isoformat()))
        current += timedelta(days=1)

    return windows
