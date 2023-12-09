class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()
        else:
            return None

class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None

class Fire:
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return None

class Earth:
    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None

class Storm:
    pass

class Steam:
    pass

class Mud:
    pass

class Lightning:
    pass

class Dust:
    pass

class Lava:
    pass


class Ice:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Water()
        elif isinstance(other, Earth):
            return Glacier()
        else:
            return None

class Glacier:
    pass


water = Water()
air = Air()
fire = Fire()
earth = Earth()
ice = Ice()

storm = water + air
print(type(storm))

glacier = ice + earth
print(type(glacier))

undefined = earth + ice
print(undefined)