from typing import Any, Callable, Optional

from engine.enums import Proximity, Sex
from engine.verbs import Verb

class GameContext():
	player: Any
	currentloc: Any
	oa: Any

class GameLocation():
	def __init__(
			self,
			ID: str = "ProtoLoc",
			Name: str = "Location Prototype",
			Children: list[Any] = [],
			Visited: int = 0,
			isJustEntered: bool = False,
			Timer: int = 0
		):
		self.ID = ID
		self.Name = Name
		self.Children = Children
		self.Visited = Visited
		self.isJustEntered = isJustEntered
		self.Timer = Timer
	def Desc(self) -> str:
		return "The object to origin all other locations."
	def Enter(self) -> str:
		return "You’ve entered Proto Location."
	def Events(self) -> str:
		return "Something’s happening."
	def Acts(self) -> str:
		return ""
	def NoGo(self) -> str:
		return "No, there is nothing to do."

class GameObject():
	def __init__(
			self,
			ID: str = "ProtoObj",
			Sex = Sex.MALE,
			Name: str = "Object Prototype",
			NameG: Optional[str] = None,
			NameD: Optional[str] = None,
			NameA: Optional[str] = None,
			NameI: Optional[str] = None,
			NameP: Optional[str] = None,
			Children: list[Any] = [],
			Parent: Optional[str] = None,
			Disabled: bool = False,
			Examined: int = 0,
			Acted: int = 0,
			Listened: int = 0,
			# Flags
			isHidden: bool = False,
			isOpen: bool = True,
			# isNear = Proximity.CLOSE,
			isOn: bool = False,
			isTakeable: bool = False,
			isDroppable: bool = False,
			isOpenable: bool = False,
			isSwitchable: bool = False,
			isTuneable: bool = False,
			isWearable: bool = False,
			isWorn: bool = False,
		):
		self.ID = ID
		self.Sex = Sex
		self.Name = Name
		self.NameG = NameG if NameG != None else Name
		self.NameD = NameD if NameD != None else Name
		self.NameA = NameA if NameA != None else Name
		self.NameI = NameI if NameI != None else Name
		self.NameP = NameP if NameP != None else Name
		self.Children = Children
		self.Parent = Parent
		self.Disabled = Disabled
		self.Examined = Examined
		self.Acted = Acted
		self.Listened = Listened
		self.isHidden = isHidden
		self.isOpen = isOpen
		# self.isNear = isNear
		self.isOn = isOn
		self.isTakeable = isTakeable
		self.isDroppable = isDroppable
		self.isOpenable = isOpenable
		self.isSwitchable = isSwitchable
		self.isTuneable = isTuneable
		self.isWearable = isWearable
		self.isWorn = isWorn
	def Desc(self):
		return "ProtoObject description."

class Loc(GameLocation):
	def __init__(self, *args, **kwds):
		super().__init__(*args, **kwds)

class Obj(GameObject):
	def __init__(self, *args, **kwds):
		super().__init__(*args, **kwds)
		self.Look: Verb = Verb()
		self.Take: Verb = Verb()
		self.Drop: Verb = Verb()
	def init_verbs(self, ctx):
		from engine.verbs import Look, Take, Drop
		self.Look = Look(obj=self)
		self.Take = Take(obj=self, ctx=ctx)
		self.Drop = Drop(obj=self, ctx=ctx)


