from engine.entities import GameLocation, GameObject

class ObjectAlteration():
    """
    Класс для управления игровыми объектами и локациями.

    Атрибуты:
    - locs: Словарь всех локаций.
    - objs: Словарь всех объектов.

    Методы:
    - removeobj: Удаляет объект из родителя и отключает его.
    - moveobj: Перемещает объект к новому родителю.
    - openobj: Открывает объект и делает его детей доступными.
    - closeobj: Закрывает объект и делает его детей недоступными.
    """
    def __init__(self, locs: dict[str, 'GameLocation'], objs: dict[str, 'GameObject']):
        self.locs = locs
        self.objs = objs
    def removeobj(self, obj: 'GameObject'):
        obj.Disabled = True
        if obj.Parent:
            _parent = self.objs[obj.Parent]
            _parent.Children.remove(obj)
            obj.FormerParent = obj.Parent
            obj.Parent = None
    def moveobj(self, obj: 'GameObject', par: 'GameObject'):
        if obj.Parent:
            _parent = self.objs[obj.Parent]
            _parent.Children.remove(obj)
            obj.FormerParent = obj.Parent
        obj.Parent = par.ID
        par.Children.append(obj)
    def openobj(self, obj: 'GameObject'):
        obj.isOpen = True
        for c in obj.Children:
            c.Disabled = False
    def closeobj(self, obj: 'GameObject'):
        obj.isOpen = False
        for c in obj.Children:
            c.Disabled = True
