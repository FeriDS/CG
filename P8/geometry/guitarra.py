from geometry.geometry import Geometry
from core.obj_reader import my_obj_reader

class GuitarraGeometry(Geometry):
    def __init__(self, width = 1, height = 1, depth = 1):
        super().__init__()
        c1, c2 = [1, 0.5, 0.5], [0.5, 0, 0]
        c3, c4 = [1, 1, 1], [0.545, 0.27, 0.075]
        c5, c6 = [0.5, 0.5, 1], [0, 0, 0.5]
        # texture coordinates
        t0, t1, t2, t3 = [0, 0], [1, 0], [0, 1], [1, 1]


        position_data = my_obj_reader("./geometry/guitarraNewVersion.obj")


        colorNumber = int(len(position_data) / 6)

        color_data = [c1] * 1799 + [c2] * 500 + [c3] * 2000 + [c4] * 10000 
        uv_data = [t0, t1, t3, t0, t3, t2] * 6
        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec3", "vertexColor", color_data)
        self.add_attribute("vec2", "vertexUV", uv_data)
        self.count_vertices()
