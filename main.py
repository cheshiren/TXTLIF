import textual
from textual.app import App, ComposeResult
from textual.content import Content
from textual.screen import Screen
from textual.widgets import Header, Markdown, MarkdownViewer, Static


class TextScreen(Screen):
	def __init__(self, name = None, id = None, classes = None, text:str=""):
		super().__init__(name, id, classes)
		self.text = text
	def compose(self) -> ComposeResult:
		yield Header()
		yield Markdown(self.text)
	def on_markdown_link_clicked(self, event: Markdown.LinkClicked) -> None:
		md = event.markdown
		new_text = md._markdown.replace("Title", "WTF") + "klsdjf;alsdkfja;lkdfj;laksdfj;alsdkfj;alsdkfj"
		md.update(new_text)

class MainApp(App):
	
	# SCREENS = {"start_screen": TextScreen}

	text = """\
# Title
dfghdkjlfg

## Title
fgdfhgfgh
[testlink](#Title)
"""

	def on_mount(self) -> ComposeResult:
		self.install_screen(TextScreen(text=self.text), "start_screen")
		self.push_screen("start_screen")

if __name__ == "__main__":
	app = MainApp()
	app.run()