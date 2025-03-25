""" Render the sine function """
import numpy as np
import pathlib
import sys


from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from geometry.geometry import Geometry
from material.point import PointMaterial
from material.line import LineMaterial


class Example(Base):
    """ Render the sine function """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.camera.set_position([0, 0, 5])
        geometry = Geometry()
        vs_code = """
        uniform mat4 projectionMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 modelMatrix;
        in vec3 vertexPosition;
        uniform float time;
        void main()
        {
            float offset = 1 * sin(1 * vertexPosition.x + time);
            vec3 pos = vertexPosition + vec3(0.0, offset, 0.0);
            gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(-pos, 1.0);
        }
        """
        fs_code = """
        uniform vec3 baseColor;
        uniform bool useVertexColors;
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(baseColor, 1.0);
        }
        """
        position_data = []
        x_values = np.arange(-3.2, 3.2, 0.2)
        y_values = np.sin(x_values)
        for x, y in zip(x_values, y_values):
            position_data.append([x, 0, 0])
        geometry.add_attribute("vec3", "vertexPosition", position_data)
        geometry.count_vertices()
        use_vertex_colors = False
        self._time = 0
        point_material = PointMaterial(vs_code, fs_code, {"baseColor": [1, 1, 1], "pointSize": 10}, 
                                        use_vertex_colors)
        point_material.add_uniform("float", "time", self._time)
        point_material.locate_uniforms()
        self.point_mesh = Mesh(geometry, point_material)
        line_material = LineMaterial(vs_code, fs_code, {"baseColor": [1, 0, 0], "lineWidth": 2}, 
                                        use_vertex_colors)
        self.line_mesh = Mesh(geometry, line_material)
        line_material.add_uniform("float", "time", self._time)
        line_material.locate_uniforms()
        self.scene.add(self.point_mesh)
        self.scene.add(self.line_mesh)

    def update(self):
        self.time += 1 / 60
        self.line_mesh.material.uniform_dict["time"].data = self.time
        self.point_mesh.material.uniform_dict["time"].data = self.time
        self.renderer.render(self.scene, self.camera)


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
