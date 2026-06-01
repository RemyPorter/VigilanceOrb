from parser import load, parse
from actions import apply
from pathlib import Path
from actions.audio import get_audio

def preload(parsed):
    for event in parsed:
        for item in event.script:
            if "play" in item:
                item["play"] = Path(item["play"])
                get_audio().preload(item["play"])
def main():
    script = load(Path("scripts/test.yaml"))
    parsed = parse(script)
    preload(parsed)
    apply(parsed[0].event_name, parsed[0].script)


if __name__ == "__main__":
    main()
