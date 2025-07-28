import enum

class Sex(enum.Enum):
    MALE = 1
    FEMALE = 2
    NEUTER = 3
    PLURAL = 4

class Proximity(enum.Enum):
    CLOSE = 1
    NEAR = 2
    NOTFAR = 3
    FAR = 4