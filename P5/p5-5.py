"""Changing color with time"""
import math
import OpenGL.GL as GL


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

def attributeColor(r, g, b, n):
    color_data = []
    for i in range(n):
        color_data.append([r, g, b])
    return color_data
    

def makeQuarterCircle(x, y, r, n, start):
    angle = math.pi / (2 * n)
    curr_angle = start;
    curr_points = [[x, y, 0.0]]
    for i in range(n):
        curr_x = x + r * math.cos(curr_angle)
        curr_y = y + r * math.sin(curr_angle)
        curr_points.append([curr_x, curr_y, 0.0])
        curr_angle += angle
    curr_x = x + r * math.cos(curr_angle)
    curr_y = y + r * math.sin(curr_angle)
    curr_points.append([curr_x, curr_y, 0.0])
    return curr_points

class Example(Base):
    """ Animate triangle changing its color """
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
        # Set up vertex array object #
        self.vao_downCircle = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_downCircle)
        position_data_downCircle = circle(0, -0.4, 0.5, 50)
        self.vertex_count_downCircle = len(position_data_downCircle)
        position_attribute_downCircle = Attribute('vec3', position_data_downCircle)
        position_attribute_downCircle.associate_variable(self.program_ref, 'position')
        # Set up uniforms
        self.translation_downCircle = Uniform('vec3', [0.0, 0.0, 0.0])
        self.translation_downCircle.locate_variable(self.program_ref, 'translation')
        self.base_color_downCircle = Uniform('vec3', [1.0, 0.0, 0.0])
        self.base_color_downCircle.locate_variable(self.program_ref, 'baseColor')




        self.vao_downCircleMiddle = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_downCircleMiddle)
        position_data_downCircleMiddle = circle(0, -0.4, 0.3, 50)
        self.vertex_count_downCircleMiddle = len(position_data_downCircleMiddle)
        position_attribute_downCircleMiddle = Attribute('vec3', position_data_downCircleMiddle)
        position_attribute_downCircleMiddle.associate_variable(self.program_ref, 'position')
        # Set up uniforms
        self.translation_downCircleMiddle = Uniform('vec3', [0.0, 0.0, 0.0])
        self.translation_downCircleMiddle.locate_variable(self.program_ref, 'translation')
        self.base_color_downCircleMiddle = Uniform('vec3', [0.0, 0.0, 0.0])
        self.base_color_downCircleMiddle.locate_variable(self.program_ref, 'baseColor')

        self.vao_upCircle = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_upCircle)
        position_data_upCircle = circle(0, 0.4, 0.5, 50)
        self.vertex_count_upCircle = len(position_data_upCircle)
        position_attribute_upCircle = Attribute('vec3', position_data_upCircle)
        position_attribute_upCircle.associate_variable(self.program_ref, 'position')
        # Set up uniforms
        self.translation_upCircle = Uniform('vec3', [0.0, 0.0, 0.0])
        self.translation_upCircle.locate_variable(self.program_ref, 'translation')
        self.base_color_upCircle = Uniform('vec3', [1.0, 0.0, 0.0])
        self.base_color_upCircle.locate_variable(self.program_ref, 'baseColor')

        self.vao_upCircleMiddle = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_upCircleMiddle)
        position_data_upCircleMiddle = circle(0, 0.4, 0.3, 50)
        self.vertex_count_upCircleMiddle = len(position_data_upCircleMiddle)
        position_attribute_upCircleMiddle = Attribute('vec3', position_data_upCircleMiddle)
        position_attribute_upCircleMiddle.associate_variable(self.program_ref, 'position')
        # Set up uniforms
        self.translation_upCircleMiddle = Uniform('vec3', [0.0, 0.0, 0.0])
        self.translation_upCircleMiddle.locate_variable(self.program_ref, 'translation')
        self.base_color_upCircleMiddle = Uniform('vec3', [0.0, 0.0, 0.0])
        self.base_color_upCircleMiddle.locate_variable(self.program_ref, 'baseColor')


        self.vao_upSmallCircle = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_upSmallCircle)
        position_data_upSmallCircle = circle(0.334, 0.62, 0.1, 50)
        self.vertex_count_upSmallCircle = len(position_data_upSmallCircle)
        position_attribute_upSmallCircle = Attribute('vec3', position_data_upSmallCircle)
        position_attribute_upSmallCircle.associate_variable(self.program_ref, 'position')
        # Set up uniforms
        self.translation_upSmallCircle = Uniform('vec3', [0.0, 0.0, 0.0])
        self.translation_upSmallCircle.locate_variable(self.program_ref, 'translation')
        self.base_color_upSmallCircle = Uniform('vec3', [1.0, 0.0, 0.0])
        self.base_color_upSmallCircle.locate_variable(self.program_ref, 'baseColor')


        self.vao_downSmallCircle = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_downSmallCircle)
        position_data_downSmallCircle = circle(-0.334, -0.62, 0.1, 50)
        self.vertex_count_downSmallCircle = len(position_data_downSmallCircle)
        position_attribute_downSmallCircle = Attribute('vec3', position_data_downSmallCircle)
        position_attribute_downSmallCircle.associate_variable(self.program_ref, 'position')
        # Set up uniforms
        self.translation_downSmallCircle = Uniform('vec3', [0.0, 0.0, 0.0])
        self.translation_downSmallCircle.locate_variable(self.program_ref, 'translation')
        self.base_color_downSmallCircle = Uniform('vec3', [1.0, 0.0, 0.0])
        self.base_color_downSmallCircle.locate_variable(self.program_ref, 'baseColor')

        self.vao_upQuarteCircle = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_upQuarteCircle)
        position_data_upQuarteCircle = makeQuarterCircle(0, 0.4, 0.5, 25, math.pi)
        self.vertex_count_upQuarteCircle = len(position_data_upQuarteCircle)
        position_attribute_upQuarteCircle = Attribute('vec3', position_data_upQuarteCircle)
        position_attribute_upQuarteCircle.associate_variable(self.program_ref, 'position')
        # Set up uniforms
        self.translation_upQuarterCircle = Uniform('vec3', [0.0, 0.0, 0.0])
        self.translation_upQuarterCircle.locate_variable(self.program_ref, 'translation')
        self.base_color_upQuarterCircle = Uniform('vec3', [1.0, 0.0, 0.0])
        self.base_color_upQuarterCircle.locate_variable(self.program_ref, 'baseColor')


        self.vao_polygonUp = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_polygonUp)
        position_data_polygonUp = [
                [0,0.4,0],
                [0.6,0.8,0],
                [0.6,0,0],
                [0.3,0,0],
                [0,0.1,0]
            ]
        self.vertex_count_polygonUp = len(position_data_polygonUp)
        position_attribute_polygonUp = Attribute('vec3', position_data_polygonUp)
        position_attribute_polygonUp.associate_variable(self.program_ref, 'position')
        # Set up uniforms
        self.translation_polygonUp = Uniform('vec3', [0.0, 0.0, 0.0])
        self.translation_polygonUp.locate_variable(self.program_ref, 'translation')
        self.base_color_polygonUp = Uniform('vec3', [0.0, 0.0, 0.0])
        self.base_color_polygonUp.locate_variable(self.program_ref, 'baseColor')


        self.vao_polygonDown = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_polygonDown)
        position_data_polygonDown = [
                [0,-0.4,0],
                [-0.6,-0.8,0],
                [-0.6,0,0],
                [-0.3,0,0],
                [0,-0.1,0]
            ]
        self.vertex_count_polygonDown = len(position_data_polygonDown)
        position_attribute_polygonDown = Attribute('vec3', position_data_polygonDown)
        position_attribute_polygonDown.associate_variable(self.program_ref, 'position')
        # Set up uniforms
        self.translation_polygonDown = Uniform('vec3', [0.0, 0.0, 0.0])
        self.translation_polygonDown.locate_variable(self.program_ref, 'translation')
        self.base_color_polygonDown = Uniform('vec3', [0.0, 0.0, 0.0])
        self.base_color_polygonDown.locate_variable(self.program_ref, 'baseColor')

        self.movementSpeed = 0.1

    def update(self):
        """ Update data """
        GL.glUseProgram(self.program_ref)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        if(self.input.isKeyPressed("up") and self.translation_downCircle.data[1] < 0.1):
            self.translation_downCircle.data[1] += self.movementSpeed
            self.translation_downSmallCircle.data[1] += self.movementSpeed
            self.translation_upCircle.data[1] += self.movementSpeed
            self.translation_upSmallCircle.data[1] += self.movementSpeed
            self.translation_upQuarterCircle.data[1] += self.movementSpeed
            self.translation_downCircleMiddle.data[1] += self.movementSpeed
            self.translation_upCircleMiddle.data[1] += self.movementSpeed
            self.translation_polygonUp.data[1] += self.movementSpeed
            self.translation_polygonDown.data[1] += self.movementSpeed

        if(self.input.isKeyPressed("left") and self.translation_downSmallCircle.data[0] > -0.5):
            self.translation_downCircle.data[0] -= self.movementSpeed
            self.translation_downSmallCircle.data[0] -= self.movementSpeed
            self.translation_upCircle.data[0] -= self.movementSpeed
            self.translation_upSmallCircle.data[0] -= self.movementSpeed
            self.translation_upQuarterCircle.data[0] -= self.movementSpeed
            self.translation_downCircleMiddle.data[0] -= self.movementSpeed
            self.translation_upCircleMiddle.data[0] -= self.movementSpeed
            self.translation_polygonUp.data[0] -= self.movementSpeed
            self.translation_polygonDown.data[0] -= self.movementSpeed

        if(self.input.isKeyPressed("down") and self.translation_upCircle.data[1] >-0.1):
            self.translation_downCircle.data[1] -= self.movementSpeed
            self.translation_downSmallCircle.data[1] -= self.movementSpeed
            self.translation_upCircle.data[1] -= self.movementSpeed
            self.translation_upSmallCircle.data[1] -= self.movementSpeed
            self.translation_upQuarterCircle.data[1] -= self.movementSpeed
            self.translation_downCircleMiddle.data[1] -= self.movementSpeed
            self.translation_upCircleMiddle.data[1] -= self.movementSpeed
            self.translation_polygonUp.data[1] -= self.movementSpeed
            self.translation_polygonDown.data[1] -= self.movementSpeed

        if(self.input.isKeyPressed("right") and self.translation_upSmallCircle.data[0] < 0.5):
            self.translation_downCircle.data[0] += self.movementSpeed
            self.translation_downSmallCircle.data[0] += self.movementSpeed
            self.translation_upCircle.data[0] += self.movementSpeed
            self.translation_upSmallCircle.data[0] += self.movementSpeed
            self.translation_upQuarterCircle.data[0] += self.movementSpeed
            self.translation_downCircleMiddle.data[0] += self.movementSpeed
            self.translation_upCircleMiddle.data[0] += self.movementSpeed
            self.translation_polygonUp.data[0] += self.movementSpeed
            self.translation_polygonDown.data[0] += self.movementSpeed


        ## Render scene
        # Reset color buffer with specified color
        GL.glBindVertexArray(self.vao_upCircle)
        self.translation_upCircle.upload_data()
        self.base_color_upCircle.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_upCircle)


        GL.glBindVertexArray(self.vao_polygonUp)
        self.translation_polygonUp.upload_data()
        self.base_color_polygonUp.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_polygonUp)

        GL.glBindVertexArray(self.vao_downCircle)
        self.translation_downCircle.upload_data()
        self.base_color_downCircle.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_downCircle)
        

        GL.glBindVertexArray(self.vao_polygonDown)
        self.translation_polygonDown.upload_data()
        self.base_color_polygonDown.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_polygonDown)

        GL.glBindVertexArray(self.vao_upQuarteCircle)
        self.translation_upQuarterCircle.upload_data()
        self.base_color_upQuarterCircle.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_upQuarteCircle)


        GL.glBindVertexArray(self.vao_upCircleMiddle)
        self.translation_upCircleMiddle.upload_data()
        self.base_color_upCircleMiddle.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_upCircleMiddle)


        GL.glBindVertexArray(self.vao_downCircleMiddle)
        self.translation_downCircleMiddle.upload_data()
        self.base_color_downCircleMiddle.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_downCircleMiddle)


        GL.glBindVertexArray(self.vao_upSmallCircle)
        self.translation_upSmallCircle.upload_data()
        self.base_color_upSmallCircle.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_upSmallCircle)


        GL.glBindVertexArray(self.vao_downSmallCircle)
        self.translation_downSmallCircle.upload_data()
        self.base_color_downSmallCircle.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_downSmallCircle)


# Instantiate this class and run the program
Example().run()
