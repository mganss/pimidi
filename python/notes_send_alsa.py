import sys
import time
import rtmidi

midiout = rtmidi.MidiOut()

if len(sys.argv) == 1:
    available_ports = midiout.get_ports()
    for i, p in enumerate(available_ports):
        print(f"#{i}: {p}")
else:
    midiout.open_port(int(sys.argv[1]))

    with midiout:
        # channel 1, middle C, velocity 112
        note_on = [0x90, 60, 112]
        note_off = [60, 0]
        for i in range(10_000):
            if ((i % 100) == 0):
                print(f"{i} notes sent")
            midiout.send_message(note_on)
            time.sleep(0.01)
            midiout.send_message(note_off)
            time.sleep(0.01)

del midiout
