from settings import *
from world_objects.chunck import Chunck

class Scene:
    def __init__(self, app):
        self.app = app
        self.chunck = Chunck(self.app)

    def update(self):
        pass

    def render(self):
        self.chunck.render()

