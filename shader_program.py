from settings import *

class ShaderProgram:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.player = app.player
        #------Shaders------
        self.chunck= self.get_program(shader_name='chunck')
        #-------------------
        self.set_uniforms_on_init()

    def set_uniforms_on_init(self):
        self.chunck['m_proj'].write(self.player.m_proj)
        self.chunck['m_model'].write(glm.mat4())

    def update(self):
        self.chunck['m_view'].write(self.player.m_view)

    def get_program(self, shader_name):
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()

        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        
        return program
