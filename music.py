import os

# Directory where MP3 files are stored on the EV3
MUSIC_DIR = "/home/robot/music/"  # Change this if your MP3 files are elsewhere

def play_mp3(filename):
    """Plays an MP3 file using madplay or aplay."""
    file_path = os.path.join(MUSIC_DIR, filename)

    if not os.path.exists(file_path):
        print("Error: " + file_path + " not found.")
        return

    # Try to play with madplay, fallback to aplay
    cmd = "madplay " + file_path + " || aplay " + file_path
    os.system(cmd)

if __name__ == "__main__":
    print("Available MP3 files:")
    files = [f for f in os.listdir(MUSIC_DIR) if f.endswith(".mp3")]

    if not files:
        print("No MP3 files found in the directory.")
    else:
        for i, file in enumerate(files, 1):
            print(str(i) + ". " + file)

        choice = input("Enter the number of the file to play: ").strip()  # Use input() for Python 3

        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(files):
                play_mp3(files[index])
            else:
                print("Invalid selection.")
        else:
            print("Please enter a valid number.")
