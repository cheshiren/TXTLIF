import inspect, sys
from typing import Any

import game
from engine.entities import GameContext, GameLocation, GameObject
from engine.enums import Proximity, Sex
from engine.helpers import ObjectAlteration

engineClasses = set()
gameClasses = set()

# собираем все классы движка
for name, obj in inspect.getmembers(sys.modules["engine.entities"]):
	if inspect.isclass(obj):
		engineClasses.add(obj)
for name, obj in inspect.getmembers(sys.modules["engine.enums"]):
	if inspect.isclass(obj):
		engineClasses.add(obj)
for name, obj in inspect.getmembers(sys.modules["engine.verbs"]):
	if inspect.isclass(obj):
		engineClasses.add(obj)

# собираем все классы игры
for name, obj in inspect.getmembers(sys.modules["game"]):
	if inspect.isclass(obj):
		gameClasses.add(obj)

# классы игры минус классы движка → только классы игровых объектов
gameClasses = gameClasses - engineClasses

# создание всех локаций и всех объектов
locs: dict[str, GameLocation] = {}
objs: dict[str, GameObject] = {}
for e in gameClasses:
	_e = e()
	if isinstance(_e, GameLocation):
		locs[_e.ID] = _e
	if isinstance(_e, GameObject):
		objs[_e.ID] = _e

# распределение «детей» по «родителям» 
for k,v in objs.items():
	if v.Parent:
		_key = v.Parent
		_parent: Any
		if _key in locs.keys():
			_parent = locs[_key]
		if _key in objs.keys():
			_parent = objs[_key]
		_parent.Children.append(v)
		# если «родитель» не открыт, все «дети» не доступны
		if hasattr(_parent, "isOpen") and not _parent.isOpen:
			v.Disabled = True

# игровой контекст
ctx: GameContext = GameContext()
ctx.player = objs["player"]
ctx.currentloc = locs["Store"]
# объект для изменения игровых объектов
ctx.oa = ObjectAlteration(locs, objs)

# инициация глаголов у всех игровых объектов
for _,v in objs.items():
	v.init_verbs(ctx=ctx)


x: GameObject = objs["frame"].Children[0]
print(x.Look)
print(x.Cut)
print(x.Take)
print(ctx.player.Children)
print(x.Drop)
print(ctx.player.Children)
print(ctx.currentloc.Children)