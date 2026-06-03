from parser import load, parse
from actions import apply
from pathlib import Path
from actions.audio import get_audio
import mido

def preload(parsed):
    for event in parsed:
        for item in event.script:
            if "play" in item:
                item["play"] = Path(item["play"])
                get_audio().preload(item["play"])

DEVICE_CONTAINS="Mini"
class Midi:
    def __init__(self):
        input_ports = mido.get_input_names()
        for port in input_ports:
            if DEVICE_CONTAINS in port:
                self._input = mido.open_input(port)
                return
    
    def spin(self, script):
        for msg in self._input:
            breakpoint()


def main():
    script = load(Path("scripts/test.yaml"))
    parsed = parse(script)
    preload(parsed)
    apply(parsed[0].event_name, parsed[0].script)


if __name__ == "__main__":
    main()
