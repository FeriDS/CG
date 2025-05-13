from geometry.geometry import Geometry
from core.obj_reader import my_obj_reader

class GuitarraMainBodyGeo(Geometry):
    def __init__(self, width = 1, height = 1, depth = 1):
        super().__init__()

        position_data, uv_data = my_obj_reader('./geometry/guitarra_mainBody.obj')


        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", uv_data)
        self.count_vertices()

class GuitarraStringsGeo(Geometry):
    def __init__(self, width = 1, height = 1, depth = 1):
        super().__init__()

        position_data, uv_data = my_obj_reader('./geometry/guitarra_stringsAndWhiteParts.obj')


        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", uv_data)
        self.count_vertices()


class GuitarraBlackPartsAndMoreGeo(Geometry):
    def __init__(self, width = 1, height = 1, depth = 1):
        super().__init__()

        position_data, uv_data = my_obj_reader('./geometry/guitarra_partesPretas.obj')


        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", uv_data)
        self.count_vertices()

