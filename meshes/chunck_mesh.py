from meshes.base_mesh import BaseMesh
from meshes.chunck_mesh_builder import build_chunck_mesh

class ChunckMesh(BaseMesh):
    def __init__(self, chunck):
        super().__init__()
        self.app = chunck.app
        self.chunck = chunck
        self.ctx = self.app.ctx
        self.program = self.app.shader_program.chunck

        self.vbo_format = '3u1 1u1 1u1'
        self.format_size = sum(int(fmt[:1]) for fmt in self.vbo_format.split())
        self.attrs = ('in_position', 'voxel_id', 'face_id')
        self.vao = self.get_vao()
    
    def get_vertex_data(self):
        mesh = build_chunck_mesh(
                chunck_voxels = self.chunck.voxels,
                format_size = self.format_size,
        )
        return mesh
