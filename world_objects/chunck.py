from settings import *
from meshes.chunck_mesh import ChunckMesh

class Chunck:
    def __init__(self, app):
        self.app = app
        self.voxels: np.array = self.build_voxels()
        self.mesh: ChunckMesh = None
        self.build_mesh()

    def build_mesh(self):
        self.mesh = ChunckMesh(self)

    def render(self):
        self.mesh.render()

    def build_voxels(self):
        #empty chunck
        voxels = np.zeros(CHUNCK_VOL, dtype='uint8')

        # Fill Chunck
        for x in range(CHUNCK_SIZE):
            for z in range(CHUNCK_SIZE):
                for y in range(CHUNCK_SIZE):
                    voxels[x + CHUNCK_SIZE * z + CHUNCK_AREA * y] = x + y + z 
        return voxels

