"""Apresenta um hexagono na janela."""
import OpenGL.GL as GL
import numpy as np 
import math
from core.base import Base
from core.utils import Utils
from core.attribute import Attribute

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
    """ Render six points in a hexagon arrangement """
    def initialize(self):
        print("Initializing program...")
        # Initialize program #
        vs_code = """
            in vec3 position;
            in vec3 vertexColor;
            out vec3 color;
            void main()
            {
                gl_Position = vec4(position.x, position.y, position.z, 1.0);
                color = vertexColor;
            }
        """
        fs_code = """
            in vec3 color;
            out vec4 fragColor;
            void main()
            {
                fragColor = vec4(color.r, color.g, color.b, 1.0);
            }
        """
        self.program_ref = Utils.initialize_program(vs_code, fs_code)
        # Render settings (optional) #
        GL.glLineWidth(6)
        # Set up vertex array object #
        # Set up vertex attribute #
        self.vao_downCircle = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_downCircle)
        position_data_downCircle = circle(0, -0.4, 0.5, 50)
        self.vertex_count_downCircle = len(position_data_downCircle)
        position_attribute_downCircle = Attribute('vec3', position_data_downCircle)
        position_attribute_downCircle.associate_variable(self.program_ref, 'position')
        color_data = attributeColor(0.727, 0.300, 0.727, self.vertex_count_downCircle)
        color_attribute_downCircle = Attribute('vec3', color_data)
        color_attribute_downCircle.associate_variable(self.program_ref, 'vertexColor')

        self.vao_downCircleMiddle = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_downCircleMiddle)
        position_data_downCircleMiddle = circle(0, -0.4, 0.3, 50)
        self.vertex_count_downCircleMiddle = len(position_data_downCircleMiddle)
        position_attribute_downCircleMiddle = Attribute('vec3', position_data_downCircleMiddle)
        position_attribute_downCircleMiddle.associate_variable(self.program_ref, 'position')
        color_data = attributeColor(0, 0.00, 0, self.vertex_count_downCircleMiddle)
        color_attribute_downCircleMiddle = Attribute('vec3', color_data)
        color_attribute_downCircleMiddle.associate_variable(self.program_ref, 'vertexColor')

        self.vao_upCircle = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_upCircle)
        position_data_upCircle = circle(0, 0.4, 0.5, 50)
        self.vertex_count_upCircle = len(position_data_upCircle)
        position_attribute_upCircle = Attribute('vec3', position_data_upCircle)
        position_attribute_upCircle.associate_variable(self.program_ref, 'position')
        color_data = attributeColor(0.727, 0.300, 0.727, self.vertex_count_upCircle)
        color_attribute_upCircle = Attribute('vec3', color_data)
        color_attribute_upCircle.associate_variable(self.program_ref, 'vertexColor')

        self.vao_upCircleMiddle = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_upCircleMiddle)
        position_data_upCircleMiddle = circle(0, 0.4, 0.3, 50)
        self.vertex_count_upCircleMiddle = len(position_data_upCircleMiddle)
        position_attribute_upCircleMiddle = Attribute('vec3', position_data_upCircleMiddle)
        position_attribute_upCircleMiddle.associate_variable(self.program_ref, 'position')
        color_data = attributeColor(0, 0, 0, self.vertex_count_upCircleMiddle)
        color_attribute_upCircleMiddle = Attribute('vec3', color_data)
        color_attribute_upCircleMiddle.associate_variable(self.program_ref, 'vertexColor')


        self.vao_upSmallCircle = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_upSmallCircle)
        position_data_upSmallCircle = circle(0.334, 0.62, 0.1, 50)
        self.vertex_count_upSmallCircle = len(position_data_upSmallCircle)
        position_attribute_upSmallCircle = Attribute('vec3', position_data_upSmallCircle)
        position_attribute_upSmallCircle.associate_variable(self.program_ref, 'position')
        color_data = attributeColor(0.727, 0.3, 0.727, self.vertex_count_upSmallCircle)
        color_attribute_upSmallCircle = Attribute('vec3', color_data)
        color_attribute_upSmallCircle.associate_variable(self.program_ref, 'vertexColor')


        self.vao_downSmallCircle = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_downSmallCircle)
        position_data_downSmallCircle = circle(-0.334, -0.62, 0.1, 50)
        self.vertex_count_downSmallCircle = len(position_data_downSmallCircle)
        position_attribute_downSmallCircle = Attribute('vec3', position_data_downSmallCircle)
        position_attribute_downSmallCircle.associate_variable(self.program_ref, 'position')
        color_data = attributeColor(0.727, 0.3, 0.727, self.vertex_count_downSmallCircle)
        color_attribute_downSmallCircle = Attribute('vec3', color_data)
        color_attribute_downSmallCircle.associate_variable(self.program_ref, 'vertexColor')






        self.vao_upQuarteCircle = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_upQuarteCircle)
        position_data_upQuarteCircle = makeQuarterCircle(0, 0.4, 0.5, 25, math.pi)
        self.vertex_count_upQuarteCircle = len(position_data_upQuarteCircle)
        position_attribute_upQuarteCircle = Attribute('vec3', position_data_upQuarteCircle)
        position_attribute_upQuarteCircle.associate_variable(self.program_ref, 'position')
        color_data = attributeColor(0.727, 0.3, 0.727, self.vertex_count_upQuarteCircle)
        color_attribute_upQuarteCircle = Attribute('vec3', color_data)
        color_attribute_upQuarteCircle.associate_variable(self.program_ref, 'vertexColor')




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
        color_data = attributeColor(0, 0, 0, self.vertex_count_polygonUp)
        color_attribute_polygonUp = Attribute('vec3', color_data)
        color_attribute_polygonUp.associate_variable(self.program_ref, 'vertexColor')


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
        color_data = attributeColor(0, 0, 0, self.vertex_count_polygonDown)
        color_attribute_polygonDown = Attribute('vec3', color_data)
        color_attribute_polygonDown.associate_variable(self.program_ref, 'vertexColor')


    def update(self):

        GL.glUseProgram(self.program_ref)
       #GL.glDrawArrays(GL.GL_LINE_LOOP, 0 , self.vertex_count)
       #GL.glDrawArrays(GL.GL_LINES, 0 , self.vertex_count)
       #GL.glDrawArrays(GL.GL_LINE_STRIP, 0 , self.vertex_count)
       #GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.vertex_count)
        GL.glBindVertexArray(self.vao_upCircle)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_upCircle)


        GL.glBindVertexArray(self.vao_polygonUp)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_polygonUp)

        GL.glBindVertexArray(self.vao_downCircle)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_downCircle)
        

        GL.glBindVertexArray(self.vao_polygonDown)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_polygonDown)




        GL.glBindVertexArray(self.vao_upQuarteCircle)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_upQuarteCircle)


        GL.glBindVertexArray(self.vao_upCircleMiddle)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_upCircleMiddle)


        GL.glBindVertexArray(self.vao_downCircleMiddle)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_downCircleMiddle)


        GL.glBindVertexArray(self.vao_upSmallCircle)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_upSmallCircle)


        GL.glBindVertexArray(self.vao_downSmallCircle)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_downSmallCircle)





# Instantiate this class and run the program
Example().run()
