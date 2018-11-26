class BasePawn:
    cords = None
    angle = 90
    armor = None
    size = 20
    draw_list = []

    def __init__(self, x, y, armor=None):
        self.cords.x = x
        self.cords.y = y
        self.armor = armor

    def set(self, attribute_name, value):
        if self.__dict__.get(attribute_name) is None:
            return False
        self.__dict__[attribute_name] = value
        return True

    def draw(self, angle):
        for draw_class in self.draw_list:
            draw_class.draw(self)


class DrawBody:
    def __init__(self):
        pass

    def draw(self, object):
        pass

