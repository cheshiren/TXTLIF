from textual.app import App, ComposeResult

from src.classes import TextScreen
from src.texts import FISH_TEXT, LONG_FISH_TEXT, Intro



class MainApp(App):

	CSS_PATH = "styles.tcss"
	TITLE = "Заголовок"

	def __init__(self, driver_class = None, css_path = None, watch_css = False, ansi_color = False):
		super().__init__(driver_class, css_path, watch_css, ansi_color)
		self.install_screen(TextScreen(text=Intro()), "text_screen")

	def on_mount(self) -> ComposeResult:
		self.push_screen("text_screen")

if __name__ == "__main__":
	app = MainApp()
	app.run()