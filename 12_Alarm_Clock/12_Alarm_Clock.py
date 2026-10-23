
from playsound3 import playsound
from pathlib import Path
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    sound_file = Path(__file__).parent / "K.mp3"

    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(
            f"{CLEAR_AND_RETURN}"
            f"Alarm will sound in: "
            f"{minutes_left:02d}:{seconds_left:02d}",
            end=""
        )

    print("\nTime's up! Playing alarm...")

    if sound_file.exists():
        playsound(str(sound_file), block=True)
        print("Alarm finished.")
    else:
        print(f"Sound file not found: {sound_file}")

minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))

total_seconds = minutes * 60 + seconds

alarm(total_seconds)
