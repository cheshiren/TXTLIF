import inspect, sys
from typing import Any

import game
import engine
from engine.entities import GameLocation, GameObject

engineClasses = set()
gameClasses = set()

for name, obj in inspect.getmembers(sys.modules["engine.entities"]):
	if inspect.isclass(obj):
		engineClasses.add(obj)

for name, obj in inspect.getmembers(sys.modules["game"]):
	if inspect.isclass(obj):
		gameClasses.add(obj)

gameClasses = gameClasses - engineClasses

locs: dict[str, Any] = {}
objs: dict[str, Any] = {}
for e in gameClasses:
	_e = e()
	if isinstance(_e, GameLocation):
		locs[_e.ID] = _e
	if isinstance(_e, GameObject):
		objs[_e.ID] = _e

print(objs.keys())
