from datetime import datetime
import argparse


def add(a, b):
    return a + b


def build_greeting(name: str = "Codex") -> str:
    ts = datetime.now().astimezone().isoformat(timespec="seconds")
    return f"{name} is working {ts}"


def greet(name: str = "Codex") -> None:
    print(build_greeting(name))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="Codex", help="Name to show in greeting")
    args = parser.parse_args()
    greet(args.name)

