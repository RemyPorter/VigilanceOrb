# Orb Controller

For a theatrical production, the set designer selected [this LED orb](https://www.michaels.com/product/color-changing-led-floating-orb-light-by-ashland-10802936). We wanted to combine it with a sound effect and allow it to be controlled by the actors without depending on the stock remote. The goal was to make it MIDI controlled.

That's what this code does.

## Prereqs

You need `ir-ctl` configured and working with an IR LED on your device. Configuring that is an exercise for the reader. If you want to record IR signals from a remote, you'll also need an IR receiver. Again, recording IR signals is an exercise for the reader. This Python script wraps calls to `ir-ctl`, so anything you record with it should also be able to be sent with it.

## Using

To run as is, you need `uv`. Then you can simply `uv run python main.py`, and it should take care of everything.

### Scripting

Scripts are a YAML file, like [show.yaml](scripts/show.yaml).

The structure is:

```yaml
action_name: # may be anything, must be unique
  key: int # the midi key that triggers this script
  script: # the series of actions we may perform
    - log: str # output a message
    - wait: float # wait this many seconds
    - play: path # the sound file we should play
    - send: (startup|success|fail|idle) # the option we want to activate
```

Your YAML file can contain any number of actions, and a script can be any sequence of the options above. 

## Modifying

You'll likely need to modify this for your own purposes. It can, ostensibly, control any IR device. If you want other signals, you'll need to record them with `ir-ctl` yourself. You can modify [the IR Codes table](actions/ir_codes.py) to include your new IR commands. This is a path. Yes, in retrospect, it would have been more flexible to make it use a path, like playing sounds does. We live and we learn. That's a good change to make, at some point.

As it stands, this code is working and fits our purpose.
