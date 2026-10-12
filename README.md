# Jarvis AI Assistant

A beginner-friendly, text-based desktop assistant written in Python. The current version runs in the terminal and uses only Python's standard library.

## Features

- Shows the current local date and time.
- Opens Google and YouTube in the default web browser.
- Lists available commands with `help`.
- Handles blank and unknown commands without stopping.
- Exits cleanly with `exit` or `quit`.
- Includes automated tests for the current command behavior.

## Requirements

- Python 3.14.2 was used to build and test this project.
- No third-party Python packages are required.
- Opening websites requires a configured default web browser.

## Setup

Open PowerShell in the project folder, then create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

The assistant uses only Python's standard library, so there are no packages to install.

If PowerShell prevents environment activation, you can run the program and tests with the environment's Python executable directly:

```powershell
.\.venv\Scripts\python.exe main.py
.\.venv\Scripts\python.exe -m unittest -v
```

## Run

With the virtual environment activated, start the assistant from the project folder:

```powershell
python main.py
```

Example commands:

```text
You: help
Jarvis: Available commands: help, date, time, google, youtube, exit, quit
You: google
Jarvis: Opening Google.
You: exit
Jarvis: Goodbye!
```

The `date` and `time` commands both display the current local date and time. The `google` and `youtube` commands open their websites in your default browser.

## Tests

Run the automated tests from the project folder:

```powershell
python -m unittest -v
```

The website tests mock the browser, so running the test suite does not open websites.

## Project Files

- `main.py` contains the assistant's command loop and responses.
- `test_main.py` contains the automated tests.

## Limitations

- Interaction is text-only; voice input and spoken responses are not implemented.
- AI question answering is not implemented.
- Website opening depends on the computer's default browser being available.

## Future Improvements

- Add voice input and spoken responses with graceful microphone error handling.
- Add optional AI question answering using environment variables for API keys.
- Improve the code organization as more features are added.
- Consider a simple graphical interface after the terminal version is stable.