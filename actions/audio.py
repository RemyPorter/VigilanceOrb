import simpleaudio as sa
from pathlib import Path

class AudioManager:
    """Manage audio files, including preloading, so we don't have to worry about timing"""
    def __init__(self):
        self.wavs = {}

    def preload(self, path:Path):
        self.wavs[str(path)] = sa.WaveObject.from_wave_file(str(path))

    def play(self, path:Path):
        self.wavs[str(path)].play()

_am = AudioManager()

def get_audio():
    """Manage this as a singleton. We only need one."""
    global _am
    return _am