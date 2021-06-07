# Abstract Building
# 1.在初始化函数中建造
class Building:
    def __init__(self):
        self.build_floor()
        self.build_size()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

    def __repr__(self):
        return "Floor: {0.floor} | Size: {0.size}".format(self)

    def __str__(self) -> str:
        return self.__repr__()


# Concrete Buildings
class House(Building):
    def build_floor(self):
        self.floor = "One"

    def build_size(self):
        self.size = "Big"


class Flat(Building):
    def build_floor(self):
        self.floor = "More than One"

    def build_size(self):
        self.size = "Small"


class ComplexBuilding:
    def __repr__(self):
        return "Floor: {0.floor} | Size: {0.size}".format(self)


class ComplexHouse(ComplexBuilding):
    def build_floor(self):
        self.floor = "One"

    def build_size(self):
        self.size = "Big and fancy"


# 2.传入类在类外面建造(当类的依赖比较复杂，例如照相机，光源，或者大多数依赖由外部模块提供时可以用)
# In some very complex cases, it might be desirable to pull out the building
# logic into another function (or a method on another class), rather than being
# in the base class '__init__'. (This leaves you in the strange situation where
# a concrete class does not have a useful constructor
def construct_building(cls):
    building = cls()
    # 这里可以加入外部依赖，例如照相机，光源等
    building.build_floor()
    building.build_size()
    return building


if __name__ == '__main__':
    print(House())
    print(Flat())
    print(construct_building(ComplexHouse))

