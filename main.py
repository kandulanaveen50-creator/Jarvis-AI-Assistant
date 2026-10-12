from datetime import datetime
import webbrowser


def main():
    print("Jarvis: Hello! I'm ready for your command.")
    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
    }

    while True:
        command = input("You: ").strip().lower()

        if not command:
            print("Jarvis: Please enter a command, or type 'help' to see the options.")
            continue

        if command in ("exit", "quit"):
            print("Jarvis: Goodbye!")
            break

        if command == "help":
            print("Jarvis: Available commands: help, date, time, google, youtube, exit, quit")
            continue

        if command in ("date", "time"):
            current_time = datetime.now()
            print(f"Jarvis: It is {current_time:%A, %B %d, %Y at %I:%M %p}.")
            continue

        if command in websites:
            try:
                browser_opened = webbrowser.open(websites[command])
            except (OSError, webbrowser.Error):
                browser_opened = False

            if browser_opened:
                print(f"Jarvis: Opening {command.title()}.")
            else:
                print("Jarvis: I couldn't open a web browser.")
            continue

        print("Jarvis: I don't know that command yet.")


if __name__ == "__main__":
    main()