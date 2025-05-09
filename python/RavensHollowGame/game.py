import curses
import time

menu = ["Start Game", "Read Lore", "Exit"]
visited_areas = []

station_choices_visited = {
    "inspect_lamp": False
}

# Typewriter effect to simulate typing out text
def typewriter_effect(stdscr, text, delay=0.03):
    for char in text:
        stdscr.addstr(char)
        stdscr.refresh()
        time.sleep(delay)

# Draw the main menu
def draw_menu(stdscr, selected_idx):
    stdscr.clear()
    stdscr.addstr(0, 0, "RAVEN'S HOLLOW")
    stdscr.addstr(1, 0, "================\n")
    for idx, option in enumerate(menu):
        if idx == selected_idx:
            stdscr.addstr(idx + 3, 0, f"> {option}", curses.A_REVERSE)
        else:
            stdscr.addstr(idx + 3, 0, f"  {option}")
    stdscr.refresh()

# Function to display choices and handle input selection
def draw_choices(stdscr, choices):
    selected = 0
    while True:
        stdscr.clear()
        for idx, choice in enumerate(choices):
            if idx == selected:
                stdscr.addstr(idx + 1, 0, f"> {choice}", curses.A_REVERSE)
            else:
                stdscr.addstr(idx + 1, 0, f"  {choice}")
        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_UP and selected > 0:
            selected -= 1
        elif key == curses.KEY_DOWN and selected < len(choices) - 1:
            selected += 1
        elif key == 10:
            return selected

# The first scene when the game starts
def introduction_scene(stdscr):
    stdscr.clear()
    typewriter_effect(stdscr, "A train arrives through the fog...\n")
    time.sleep(1)
    typewriter_effect(stdscr, "You step off into the forgotten town of Raven's Hollow.\n")
    time.sleep(1)
    typewriter_effect(stdscr, "You're an investigator looking for Mary Shaw's lost research.\n")
    time.sleep(1)

    choice = draw_choices(stdscr, ["Enter the town", "Go back"])
    if choice == 0:
        old_train_station(stdscr)
    else:
        stdscr.clear()
        typewriter_effect(stdscr, "You decide this was a mistake...\n")
        time.sleep(2)

# The old train station scene
def old_train_station(stdscr):
    if "Train Station" not in visited_areas:
        visited_areas.append("Train Station")
    stdscr.clear()
    typewriter_effect(stdscr, "You are at the old train station. Rusted signs. A broken lamp flickers.\n")
    while True:
        choice = draw_choices(stdscr, ["Walk to the abandoned street", "Inspect the lamp", "Go back to platform"])
        if choice == 0:
            abandoned_street(stdscr)
            return
        elif choice == 1:
            stdscr.clear()
            if not station_choices_visited["inspect_lamp"]:
                typewriter_effect(stdscr, "You find a shard of glass and... a number etched in the pole: 3\n")
                station_choices_visited["inspect_lamp"] = True
            else:
                typewriter_effect(stdscr, "The lamp continues to flicker. A faint hum pulses from within.\n")
            stdscr.getch()
        else:
            introduction_scene(stdscr)
            return

# The abandoned street scene
def abandoned_street(stdscr):
    if "Abandoned Street" not in visited_areas:
        visited_areas.append("Abandoned Street")
    stdscr.clear()
    typewriter_effect(stdscr, "The street is silent. Windows are boarded up. You hear a distant creak.\n")
    choice = draw_choices(stdscr, ["Enter the theater ruins", "Return to the station"])
    if choice == 0:
        theater_ruins(stdscr)
    else:
        old_train_station(stdscr)

# The theater ruins scene
def theater_ruins(stdscr):
    if "Theater Ruins" not in visited_areas:
        visited_areas.append("Theater Ruins")
    stdscr.clear()
    typewriter_effect(stdscr, "The air is thick. Dust dances through faint rays of light.\n")
    typewriter_effect(stdscr, "Something whispers your name...\n")
    stdscr.getch()

# Main function to run the game
def main(stdscr):
    curses.curs_set(0)
    selected_idx = 0

    while True:
        draw_menu(stdscr, selected_idx)
        key = stdscr.getch()

        if key == curses.KEY_UP and selected_idx > 0:
            selected_idx -= 1
        elif key == curses.KEY_DOWN and selected_idx < len(menu) - 1:
            selected_idx += 1
        elif key == 10:
            if menu[selected_idx] == "Exit":
                break
            elif menu[selected_idx] == "Start Game":
                introduction_scene(stdscr)
            elif menu[selected_idx] == "Read Lore":
                stdscr.clear()
                typewriter_effect(stdscr, "Mary Shaw was once a scientist obsessed with life beyond death.\n")
                stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
