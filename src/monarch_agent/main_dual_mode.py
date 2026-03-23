from monarch_agent.config import generate_stay_windows, load_config
from monarch_agent.marriott_checker_v2 import check_availability
from monarch_agent.state import load_state, save_state


BOOKING_MODES = ("cash", "points")


def run() -> None:
    config = load_config()
    windows = generate_stay_windows(config)

    state = load_state()
    seen = state.get("seen", {})
    changes = []

    for booking_mode in BOOKING_MODES:
        for window in windows:
            result = check_availability(window, config)
            result["booking_mode"] = booking_mode
            fingerprint = result.get("fingerprint", "") + booking_mode
            key = f"{booking_mode}_{window.check_in}_{window.check_out}"

            if seen.get(key) != fingerprint:
                seen[key] = fingerprint
                changes.append(result)

    state["seen"] = seen
    save_state(state)

    if changes:
        print("CHANGES FOUND")
        for item in changes:
            print(item)
    else:
        print("No changes across cash and points windows")


if __name__ == "__main__":
    run()
