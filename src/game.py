
from engine.entities import Loc, Obj
from engine.enums import Proximity, Sex
from engine.verbs import Look, Verb


class Store(Loc):
	def __init__(self):
		super().__init__(ID = "Store", Name = "У тела гончей")
	def Desc(self):
		return "<<obj 'Тело гончей' $body>> лежит в дымящейся <<prop 'луже нейроколлагена' $puddleNC>>, смешанного с многолетней <<prop 'пылью' $dust>>, что покрывает толстым слоем <<prop 'пол' $floor>> древнего <<prop 'цеха' $storeProp>>.<br>"
	def Acts(self):
		return """Act1
		Act2
		Act3"""

locsArray: list[Loc] = [Store()]
print (locsArray[0].Desc())

class Thing(Obj):
	def __init__(self):
		super().__init__(
			ID = "Thing",
			Name = "штука",
			NameA = "штуку"
		)
		self.Look.AddAct = self.lookAddAct
	def lookAddAct(self):
		self.Examined += 11

class frame(Obj):
	def __init__(self):
		super().__init__(ID="frame", Parent=Store)
class frameCover(Obj):
	def __init__(self):
		super().__init__(
			ID = "frameCover",
			Name = "арахно-плёнка корпуса",
			NameG = "арахно-плёнки корпуса",
			NameD = "арахно-плёнке корпуса",
			NameA = "арахно-плёнку корпуса",
			NameI = "арахно-плёнкой корпуса",
			NameP = "арахно-плёнке корпуса",
			Sex = Sex.FEMALE,
			Parent = frame
		)
		self.Cut = Verb(self)
		self.Cut.Outcome = self.CutOutcome
		self.Cut.AfterAct = self.CutAfterAct
		self.isCut = False
	def Desc(self):
		return "Серая плёнка, обтянувшая <<obj 'корпус гончей' $body>>, сплетена из микронных нитей металла и искусственной паутины, что придаёт ей огромный запас прочности, пусть и с некоторой потерей гибкости — идеальное сочетание для корпуса, в котором спрятана энергоустановка."
	# def CutAct(self):
	# 	pass
	def CutOutcome(self):
		if not self.isCut:
			return "* подрезал плёнку корпуса *"
		else:
			return "* плёнка корпуса уже подрезана *"
	def CutAfterAct(self):
		self.isCut = True

x = Thing()
xx = frameCover()

print(x.Look())
print(x.Examined)
print(xx.Cut())
print(xx.Cut())
