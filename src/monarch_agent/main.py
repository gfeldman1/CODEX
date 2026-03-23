from datetime import datetime
from monarch_agent.marriott_checker import check_availability
from monarch_agent.state import load_state, save_state


def run():
    state = load_state()

    result = check_availability()

    last = state.get("last")

    if last != result["fingerprint"]:
        print("CHANGE DETECTED")
        print(result)
        state["last"] = result["fingerprint"]
        save_state(state)
    else:
        print("No change")


if __name__ == "__main__":
    run()
