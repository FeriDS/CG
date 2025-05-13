from geometry.geometry import Geometry
from core.obj_reader import my_obj_reader


class CastanetsGeometryUp(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data, uv_data = my_obj_reader('./geometry/castanetsv2WIP_cima.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", uv_data)
        self.count_vertices()



class CastanetsGeometryDown(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data, uv_data = my_obj_reader('./geometry/castanetsv2WIP_baixo.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", uv_data)
        self.count_vertices()

