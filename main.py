from visual import Window


def main():
    """Creates and displays a 800x600 pixel window untill the user closes it."""
    win = Window(800, 600)
    win.wait_for_close()
    

if __name__ == "__main__":
    main()

    