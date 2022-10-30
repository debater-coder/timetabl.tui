from time import monotonic

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Button, Header, Footer, Static


class TimetablApp(App):
    """A Textual app to show your SBHS timetable."""

    CSS_PATH = "main.css"

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),

    ]

    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = TimetablApp()
    app.run()
