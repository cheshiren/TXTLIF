from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.screen import Screen
from textual.widget import Widget
from textual.widgets import Header, Static


class TextScreen(Screen):
	def __init__(self, name=None, id=None, classes=None, text: str | Widget = "БЛОК ТЕКСТА"):
		super().__init__(name, id, classes)
		self.text = text

	def compose(self) -> ComposeResult:
		yield Header()
		with VerticalScroll():
			if isinstance(self.text, str):
				yield Static(self.text)
			else:
				yield self.text

class StoryButton():
	def __init__(self, label: str = "EMPTY BUTTON LABEL", target: str = "EMPTY TARGET"):
		self.label = label
		self.target = target

class StoryBit():
	def __init__(
		self,
		label: str = "EMPTY LABEL",
		text: str = "EMPTY TEXT",
		commands: list[str] = [],
		buttons: list[StoryButton] = []
	):
		self.label: str = label
		self.text: str = text
		self.commands: list[str] = commands
		self.buttons: list[StoryButton] = buttons
	def __str__(self):
		return (f"{self.label}\n{self.text}\n{self.commands}\n{self.buttons}\n")


