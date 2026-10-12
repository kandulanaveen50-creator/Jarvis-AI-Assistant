import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import call, patch

import main


class JarvisCommandTests(unittest.TestCase):
    def run_assistant(self, commands):
        output = StringIO()
        with patch("builtins.input", side_effect=commands):
            with redirect_stdout(output):
                main.main()
        return output.getvalue()

    def test_blank_input_prompts_for_a_command(self):
        output = self.run_assistant(["   ", "exit"])

        self.assertIn("Please enter a command", output)

    def test_help_lists_available_commands(self):
        output = self.run_assistant(["help", "exit"])

        self.assertIn("help, date, time, google, youtube, exit, quit", output)

    def test_unknown_command_gets_a_response(self):
        output = self.run_assistant(["dance", "exit"])

        self.assertIn("I don't know that command yet", output)

    def test_date_and_time_commands_return_responses(self):
        output = self.run_assistant(["date", "time", "exit"])

        self.assertEqual(output.count("Jarvis: It is "), 2)

    def test_website_commands_open_the_expected_urls(self):
        with patch("main.webbrowser.open", return_value=True) as open_browser:
            self.run_assistant(["google", "youtube", "exit"])

        self.assertEqual(
            open_browser.call_args_list,
            [
                call("https://www.google.com"),
                call("https://www.youtube.com"),
            ],
        )

    def test_browser_failures_do_not_stop_the_assistant(self):
        failures = [False, OSError("browser unavailable"), main.webbrowser.Error("no browser")]
        with patch("main.webbrowser.open", side_effect=failures):
            output = self.run_assistant(["google", "youtube", "google", "exit"])

        self.assertEqual(output.count("I couldn't open a web browser"), 3)
        self.assertIn("Goodbye!", output)


if __name__ == "__main__":
    unittest.main()