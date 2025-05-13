from geometry.geometry import Geometry
from core.obj_reader import my_obj_reader

class TreeMainBodyGeo(Geometry):
    def __init__(self, width = 1, height = 1, depth = 1):
        super().__init__()

        position_data, uv_data = my_obj_reader('./geometry/Tree_body.obj')


        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", uv_data)
        self.count_vertices()

class TreeLeavesGeo(Geometry):
    def __init__(self, width = 1, height = 1, depth = 1):
        super().__init__()

        position_data, uv_data = my_obj_reader('./geometry/Tree_leaves.obj')


        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", uv_data)
        self.count_vertices()


