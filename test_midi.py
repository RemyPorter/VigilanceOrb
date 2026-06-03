import mido

DEVICE_NAME = "'MPK Mini Mk II:MPK Mini Mk II MIDI 1 28:0'" 

input_ports = mido.get_input_names()
print(input_ports)
with mido.open_input(input_ports[1]) as inport:
  for msg in inport:
    print(msg)

