from pathlib import Path
from subprocess import call

IR_CODES = {
    "startup": "messages/startup.msg",
    "fail": "messages/fail.msg",
    "idle": "messages/idle.msg",
    "success": "messages/success.msg"
}

def send_ir(code:str):
    file = IR_CODES.get(code, "idle")
    call(["ir-ctl", "-d", "/dev/lirc0", "-s", file])
