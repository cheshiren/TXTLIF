
# from entities import Object
class Verb():
	def __init__(
			self,
			obj,
			link: str = "ProtoVerb",
		):
		self.link = link
		self.obj = obj
	def Act(self):
		pass
	def AddAct(self):
		pass
	def Outcome(self):
		return f"Some action on {self.obj.Name}"
	def AfterAct(self):
		pass
	def __call__(self, *args, **kwds):
		self.Act()
		# self.AddAct()
		outcome = self.Outcome()
		self.AfterAct()
		return outcome

class Look(Verb):
	def __init__(self, obj, link = "Осмотреть"):
		super().__init__(obj, link)
	def Act(self):
		self.obj.Examined += 1
	def Outcome(self):
		return f"Осмотрел {self.obj.NameA}"