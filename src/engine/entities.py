from typing import Any, Callable, Optional

from engine.enums import Proximity, Sex
from engine.verbs import Verb

class GameContext():
    """
    Класс игрового контекста.

    Атрибуты:
    - player: Игрок.
    - currentloc: Текущая локация.
    - oa: Объект для управления объектами.
    """
    player: any
    currentloc: any
    oa: any

class GameLocation():
    """
    Базовый класс для всех локаций.

    Атрибуты:
    - ID: Идентификатор локации.
    - Name: Название локации.
    - Children: Список дочерних объектов.
    - Visited: Счетчик посещений.
    - isJustEntered: Флаг входа.
    - Timer: Таймер.

    Методы:
    - Desc: Описание локации.
    - Enter: Действие при входе.
    - Events: События в локации.
    - Acts: Доступные действия.
    - NoGo: Сообщение при невозможности действия.
    """
    def __init__(
            self,
            ID: str = "ProtoLoc",
            Name: str = "Location Prototype",
            Children: list = [],
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
    """
    Базовый класс для всех игровых объектов.

    Атрибуты:
    - ID: Идентификатор объекта.
    - Sex: Род объекта.
    - Name: Имя объекта.
    - NameG, NameD, NameA, NameI, NameP: Склонения имени.
    - Children: Дочерние объекты.
    - Parent: Родительский объект.
    - Disabled: Флаг доступности.
    - Examined: Счетчик осмотров.
    - Acted: Счетчик действий.
    - Listened: Счетчик прослушиваний.
    - isHidden, isOpen, isOn, isTakeable, isDroppable, isOpenable, isSwitchable, isTuneable, isWearable, isWorn: Флаги состояния.

    Методы:
    - Desc: Описание объекта.
    """
    def __init__(
            self,
            ID: str = "ProtoObj",
            Sex = None,
            Name: str = "Object Prototype",
            NameG: str = None,
            NameD: str = None,
            NameA: str = None,
            NameI: str = None,
            NameP: str = None,
            Children: list = [],
            Parent: str = None,
            Disabled: bool = False,
            Examined: int = 0,
            Acted: int = 0,
            Listened: int = 0,
            isHidden: bool = False,
            isOpen: bool = True,
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
    """
    Класс игровой локации, наследует GameLocation.
    """
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)

class Obj(GameObject):
    """
    Класс игрового объекта, наследует GameObject.

    Атрибуты:
    - Look: Глагол осмотра.
    - Take: Глагол взятия.
    - Drop: Глагол бросания.

    Методы:
    - init_verbs: Инициализация глаголов для объекта.
    """
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.Look = None
        self.Take = None
        self.Drop = None
    def init_verbs(self, ctx):
        from engine.verbs import Look, Take, Drop
        self.Look = Look(obj=self)
        self.Take = Take(obj=self, ctx=ctx)
        self.Drop = Drop(obj=self, ctx=ctx)


