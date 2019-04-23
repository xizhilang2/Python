class Scene(object):
    """docstring for Scene."""

    def __init__(self, arg):
        super(Scene, self).__init__()
        self.arg = arg

    def enter(self):
        pass

class Engine(object):
    """docstring for Engine."""

    def __init__(self, scene_map):
        super(Engine, self).__init__()
        self.scene_map = scene_map

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):
    """docstring for Map."""

    def __init__(self, start_scene):
        super(Map, self).__init__()
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
