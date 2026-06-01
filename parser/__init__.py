from pathlib import Path
from ruamel.yaml import YAML
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class Script:
    event_name:str
    midi_trigger:int
    script:List[Dict[str,Any]]

def load(path:Path):
    y = YAML(typ="safe")
    return y.load((path.open()))

def parse(loaded:dict):
    return [
        Script(name,v["key"],v["script"])
        for name,v in loaded.items()
    ]