import time
from typing import Dict, Callable, List, Any
from .ir_codes import send_ir
from .audio import get_audio

"""Actions we want to perform"""

def wait(secs:float):
    log(f"Waiting {secs} seconds")
    time.sleep(secs)

def log(msg:str):
    print(msg)

def send(ir_code:str):
    log(f"Sending IR command {ir_code}")
    send_ir(ir_code)

def play(audio_file:str):
    log(f"Playing {audio_file}")
    get_audio().play(audio_file)

ACTION_MAP:Dict[str,Callable] = {
    "wait": wait,
    "log": log,
    "play": play,
    "send": send
}

def apply(event_name:str, script:List[Dict[str,Any]]):
    log(f"Triggering {event_name}...")
    for action in script:
        for name,params in action.items():
            if name in ACTION_MAP:
                ACTION_MAP[name](params)
            else:
                log(params)
    log(f"{event_name} complete")