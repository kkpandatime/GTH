from enum import Enum
from abc import ABC, abstractmethod

class ClothType(Enum):
    COAT = 0
    COSTUME = 1

class ACloth(ABC):

    name: str
    type: 'ClothType'

    def __init__(self, name: str, cloth_type: 'ClothType') -> None:
        self.name = name
        self.type = cloth_type

class Coat(ACloth):
    size: float

    def __init__(self, name: str, size: float) -> None:
        super().__init__(name, ClothType.COAT)
        self.size = size

    def calc_cloth(self) -> float:
        return self.size / 6.5 + 0.5


class Costume(ACloth):
    height: float

    def __init__(self, name: str, height) -> None:
        super().__init__(name, ClothType.COSTUME)
        self.height = height

    def calc_cloth(self) -> float:
        return 2 * self.height + 0.3
