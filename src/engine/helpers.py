from engine.entities import GameLocation, GameObject

class ObjectAlteration():
	def __init__(self, locs: dict[str, GameLocation], objs: dict[str, GameObject]):
		self.locs = locs
		self.objs = objs
	def removeobj(self, obj: GameObject):
		obj.Disabled = True
		if obj.Parent:
			_parent = self.objs[obj.Parent]
			_parent.Children.remove(obj)
			obj.FormerParent = obj.Parent
			obj.Parent = None
	def moveobj(self, obj: GameObject, par: GameObject):
		if obj.Parent:
			_parent = self.objs[obj.Parent]
			_parent.Children.remove(obj)
			obj.FormerParent = obj.Parent
		obj.Parent = par.ID
		par.Children.append(obj)
	def openobj(self, obj: GameObject):
		obj.isOpen = True
		for c in obj.Children:
			c.Disabled = False
	def closeobj(self, obj: GameObject):
		obj.isOpen = False
		for c in obj.Children:
			c.Disabled = True
