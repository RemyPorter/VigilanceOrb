from parser import load, parse
from actions import apply
from pathlib import Path
from actions.audio import get_audio
import mido

def preload(parsed):
    for event in parsed.values():
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
        raise Exception("NO MIDI!")
    
    def spin(self, script):
        for msg in self._input:
            if msg.type == "note_on":
                continue
            if msg.note in script:
                print(f"Note {msg.note} received")
                apply(script[msg.note].event_name, script[msg.note].script)
                print("Script applied")



def main():
    script = load(Path("scripts/show.yaml"))
    parsed = parse(script)
    preload(parsed)
    m = Midi()
    m.spin(parsed)


if __name__ == "__main__":
    main()
