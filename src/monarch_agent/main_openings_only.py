from monarch_agent.config import generate_stay_windows, load_config
from monarch_agent.marriott_checker_v2 import check_availability
from monarch_agent.state import load_state, save_state


BOOKING_MODES = ("cash", "points")
OPEN_STATUSES = {"POSSIBLE_MATCH", "AVAILABLE"}


def run() -> None:
    config = load_config()
    windows = generate_stay_windows(config)

    state = load_state()
    seen = state.get("seen", {})
    opened = []

    for booking_mode in BOOKING_MODES:
        for window in windows:
            result = check_availability(window, config)
            result["booking_mode"] = booking_mode
            key = f"{booking_mode}_{window.check_in}_{window.check_out}"
            previous = seen.get(key, {})
            previous_status = previous.get("status") if isinstance(previous, dict) else None

            current_snapshot = {
                "status": result.get("status"),
                "matches": result.get("matches", []),
                "fingerprint": result.get("fingerprint", ""),
            }

            if result.get("status") in OPEN_STATUSES and previous_status not in OPEN_STATUSES:
                opened.append(result)

            seen[key] = current_snapshot

    state["seen"] = seen
    save_state(state)

    if opened:
        print("NEW ROOM OPENINGS")
        for item in opened:
            print(item)
    else:
        print("No new room openings")


if __name__ == "__main__":
    run()
