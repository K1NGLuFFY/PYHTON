import json
import os
import sys
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
DATA_FILE = os.path.join(DATA_DIR, "queue.json")


def now_utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def format_local(dt_iso: str) -> str:
    try:
        dt = datetime.fromisoformat(dt_iso)
        # Convert to local timezone for display
        local_dt = dt.astimezone()
        return local_dt.strftime("%Y-%m-%d %H:%M:%S %Z")
    except Exception:
        return dt_iso


def ensure_data_file() -> None:
    if not os.path.isdir(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(DATA_FILE):
        default = {"next_id": 1, "queue": [], "history": []}
        save_data(default)


def load_data() -> Dict[str, Any]:
    ensure_data_file()
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data: Dict[str, Any]) -> None:
    if not os.path.isdir(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def add_person(name: str) -> Dict[str, Any]:
    name = name.strip()
    if not name:
        raise ValueError("Name cannot be empty.")
    data = load_data()
    ticket_id = data.get("next_id", 1)
    entry = {
        "id": ticket_id,
        "name": name,
        "joined_at": now_utc_iso(),
    }
    data.setdefault("queue", []).append(entry)
    data["next_id"] = ticket_id + 1
    save_data(data)
    return entry


def call_next() -> Optional[Dict[str, Any]]:
    data = load_data()
    queue: List[Dict[str, Any]] = data.get("queue", [])
    if not queue:
        return None
    person = queue.pop(0)
    person_called = dict(person)
    person_called["called_at"] = now_utc_iso()
    data.setdefault("history", []).append(person_called)
    data["queue"] = queue
    save_data(data)
    return person_called


def get_position(ticket_id: int) -> Optional[int]:
    data = load_data()
    for idx, p in enumerate(data.get("queue", []), start=1):
        if p["id"] == ticket_id:
            return idx
    return None


def view_queue() -> None:
    data = load_data()
    queue: List[Dict[str, Any]] = data.get("queue", [])
    count = len(queue)
    print("")
    print(f"Total waiting: {count}")
    if count == 0:
        print("Queue is empty.")
        return

    # Show next two up front
    print("Next up:")
    first = queue[0]
    print(f"  1) #{first['id']} - {first['name']} (joined {format_local(first['joined_at'])})")
    if count >= 2:
        second = queue[1]
        print(f"  2) #{second['id']} - {second['name']} (joined {format_local(second['joined_at'])})")

    # Full list
    print("")
    print("Full waiting list:")
    for idx, person in enumerate(queue, start=1):
        print(f"  {idx:>3}. #{person['id']:<4} {person['name']:<20} joined {format_local(person['joined_at'])}")


def find_person(query: str) -> List[Dict[str, Any]]:
    data = load_data()
    queue: List[Dict[str, Any]] = data.get("queue", [])
    history: List[Dict[str, Any]] = data.get("history", [])

    results: List[Dict[str, Any]] = []

    if query.isdigit():
        tid = int(query)
        for p in queue:
            if p["id"] == tid:
                results.append({"status": "waiting", **p})
        for p in history:
            if p["id"] == tid:
                results.append({"status": "called", **p})
    else:
        ql = query.strip().lower()
        for p in queue:
            if p["name"].lower() == ql:
                results.append({"status": "waiting", **p})
        for p in history:
            if p["name"].lower() == ql:
                results.append({"status": "called", **p})

    return results


def print_person_results(results: List[Dict[str, Any]]) -> None:
    if not results:
        print("No matching person found.")
        return
    data = load_data()
    queue_ids = [p["id"] for p in data.get("queue", [])]

    for r in results:
        status = r.get("status", "?")
        tid = r["id"]
        name = r["name"]
        if status == "waiting":
            pos = queue_ids.index(tid) + 1 if tid in queue_ids else None
            joined = format_local(r["joined_at"]) if r.get("joined_at") else "?"
            print(f"Waiting: #{tid} - {name} at position {pos}. Joined {joined}.")
        elif status == "called":
            joined = format_local(r["joined_at"]) if r.get("joined_at") else "?"
            called = format_local(r["called_at"]) if r.get("called_at") else "?"
            print(f"Already called: #{tid} - {name}. Joined {joined}. Called {called}.")
        else:
            print(f"#{tid} - {name} (status unknown)")


def reset_all(confirm: bool = False) -> None:
    if not confirm:
        print("Reset cancelled.")
        return
    save_data({"next_id": 1, "queue": [], "history": []})
    print("All data cleared.")


def menu() -> None:
    while True:
        print("")
        print("==== Name Tally / Queue App ====")
        print("1) Add new person")
        print("2) View waiting list")
        print("3) Call next person")
        print("4) Find a person (by name or ticket #)")
        print("5) Reset all data")
        print("0) Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            name = input("Enter person's name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            try:
                entry = add_person(name)
                pos = get_position(entry["id"]) or "?"
                print(f"Added: #{entry['id']} - {entry['name']} at position {pos}.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            view_queue()
        elif choice == "3":
            person = call_next()
            if not person:
                print("Queue is empty. No one to call.")
            else:
                print("")
                print("Calling next:")
                print(f"  #{person['id']} - {person['name']}")
        elif choice == "4":
            q = input("Enter name or ticket #: ").strip()
            results = find_person(q)
            print_person_results(results)
        elif choice == "5":
            confirm = input("Type YES to confirm reset: ").strip()
            reset_all(confirm == "YES")
        elif choice == "0":
            print("Exiting.")
            break
        else:
            print("Invalid option. Please choose from the menu.")


if __name__ == "__main__":
    try:
        ensure_data_file()
        menu()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
        sys.exit(0)
