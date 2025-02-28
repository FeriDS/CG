"""Animation example"""
import OpenGL.GL as GL
import math
import random
from numpy import random
from core.base import Base
from core.utils import Utils
from core.attribute import Attribute
from core.uniform import Uniform


def circle(x,y,r,n):
    position_data = []
    for i in range(n):
        angle = 2*math.pi * i / n
        x_c = x + r * math.cos(angle)
        y_c = y + r * math.sin(angle)
        position_data.append([x_c, y_c, 0.0])
    return position_data

class Example(Base):
    """ Animate triangle moving across screen """
    def initialize(self):
        print("Initializing program...")
        # Initialize program #
        vs_code = """
            in vec3 position;
            uniform vec3 translation;
            void main()
            {
                vec3 pos = position + translation;
                gl_Position = vec4(pos.x, pos.y, pos.z, 1.0);
            }
        """
        fs_code = """
            uniform vec3 baseColor;
            out vec4 fragColor;
            void main()
            {
                fragColor = vec4(baseColor.r, baseColor.g, baseColor.b, 1.0);
            }
        """
        self.program_ref = Utils.initialize_program(vs_code, fs_code)
        # render settings (optional) #
        # Specify color used when clearly
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)
        # Set up vertex array object #
        vao_ref = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vao_ref)
        # Set up vertex attribute #
        position_data = circle(0.0, 0.0, 0.5, 100) 
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program_ref, 'position')
        # Set up uniforms #
        self.translation = Uniform('vec3', [0.0, -1.1, 0.0])
        self.translation.locate_variable(self.program_ref, 'translation')
        self.base_color = Uniform('vec3', [0.0, 0.1, 0.1])
        self.base_color.locate_variable(self.program_ref, 'baseColor')
        self.current = 1;

    def update(self):
        """ Update data """
        # Increase x coordinate of translation
        self.translation.data[1] += 0.01
        # If triangle passes off-screen on the right,
        # change translation, so it reappears on the left
        
        if self.translation.data[1] > 1.5:
            self.translation.data[1] = -1.5
        
        if (self.current == 0):
            self.base_color.data[2] -= 0.01
            self.base_color.data[0] += 0.01
            if (self.base_color.data[2] <= 0.0 or self.base_color.data[0] >= 1.0):
                self.base_color.data[2] = 0.0
                self.base_color.data[0] = 1.0
                self.current = 1
        if (self.current == 1):
            self.base_color.data[0] -= 0.01
            self.base_color.data[1] += 0.01
            if (self.base_color.data[0] <= 0.0 or self.base_color.data[1] >= 1.0):
                self.base_color.data[0] = 0.0
                self.base_color.data[1] = 1.0
                self.current = 2
        if (self.current == 2):
            self.base_color.data[1] -= 0.01
            self.base_color.data[2] += 0.01
            if (self.base_color.data[1] <= 0.0 or self.base_color.data[2] >= 1.0):
                self.base_color.data[1] = 0.0
                self.base_color.data[2] = 1.0
                self.current = 0
        # Render scene #
        # Reset color buffer with specified color
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glUseProgram(self.program_ref)
        self.translation.upload_data()
        self.base_color.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count)


# Instantiate this class and run the program
Example().run()
