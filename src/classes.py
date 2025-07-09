from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.screen import Screen
from textual.widget import Widget
from textual.widgets import Header, Static

class TextScreen(Screen):
	def __init__(self, name = None, id = None, classes = None, text:str|Widget="БЛОК ТЕКСТА"):
		super().__init__(name, id, classes)
		self.text = text
	def compose(self) -> ComposeResult:
		yield Header()
		with VerticalScroll():
			if isinstance(self.text, str):
				yield Static(self.text)
			else:
				yield self.text