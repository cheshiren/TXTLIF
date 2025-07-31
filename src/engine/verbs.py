class Verb():
    """
    Базовый класс для всех глаголов/действий в игре.

    Атрибуты:
    - ctx: Контекст игры, если требуется.
    - link: Имя глагола.
    Методы:
    - Act: Основное действие.
    - AddAct: Дополнительная логика действия.
    - Outcome: Результат действия.
    - AfterAct: Логика после действия.
    - __call__: Вызов действия.
    - __str__: Строковое представление результата.
    """
    def __init__(
            self,
            ctx = None,
            link: str = "ProtoVerb",
        ):
        self.ctx = ctx
        self.link = link
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
    def __str__(self):
        return self.__call__()

class Look(Verb):
    """
    Глагол для осмотра объектов.

    Атрибуты:
    - obj: Игровой объект для осмотра.
    Методы:
    - Act: Увеличивает счетчик осмотров.
    - Outcome: Возвращает строку результата осмотра.
    """
    def __init__(self, obj, link = "Осмотреть"):
        super().__init__(link)
        from engine.entities import GameObject
        self.obj:GameObject = obj
    def Act(self):
        self.obj.Examined += 1
    def Outcome(self):
        return f"Осмотрел {self.obj.NameA}"

class Take(Verb):
    """
    Глагол для взятия объектов.

    Атрибуты:
    - obj: Игровой объект для взятия.
    - ctx: Контекст игры.
    Методы:
    - Act: Перемещает объект в инвентарь игрока.
    - Outcome: Возвращает строку результата взятия.
    - AfterAct: Сброс флага justTook.
    """
    def __init__(self, obj, ctx, link = "Взять"):
        super().__init__(link)
        from engine.entities import GameContext, GameObject
        self.obj: GameObject = obj
        self.ctx: GameContext = ctx
    def Act(self):
        self.ctx.oa.moveobj(self.obj, self.ctx.player)
        self.obj.justTook = True
    def Outcome(self):
        return f"Взял {self.obj.NameA}"
    def AfterAct(self):
        self.obj.justTook = False

class Drop(Verb):
    """
    Глагол для бросания объектов.

    Атрибуты:
    - obj: Игровой объект для бросания.
    - ctx: Контекст игры.
    Методы:
    - Act: Перемещает объект в текущую локацию.
    - Outcome: Возвращает строку результата бросания.
    """
    def __init__(self, obj, ctx, link = "Взять"):
        super().__init__(link)
        from engine.entities import GameContext, GameObject
        self.obj: GameObject = obj
        self.ctx: GameContext = ctx
    def Act(self):
        self.ctx.oa.moveobj(self.obj, self.ctx.currentloc)
    def Outcome(self):
        return f"Бросил {self.obj.NameA}"