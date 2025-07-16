import curses

def main(stdscr):
    # Clear the screen
    stdscr.clear()

    # Turn off cursor
    curses.curs_set(0)

    # Add a message in the center of the screen
    height, width = stdscr.getmaxyx()
    message = "Hello from curses! Press 'q' to exit.✅"
    x = width // 2 - len(message) // 2
    y = height // 2
    stdscr.addstr(y, x, message)

    # Refresh the screen
    stdscr.refresh()

    # Wait for user input
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

# Run the program
curses.wrapper(main)

