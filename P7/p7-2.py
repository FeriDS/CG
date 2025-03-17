"""An example of a basic scene: spinning cube"""

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from geometry.box2 import BoxGeometry
from material.surface import SurfaceMaterial
from material.point import PointMaterial


class Example(Base):
    """ Render a basic scene that consists of a spinning cube """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=int(800/600))
        self.camera.set_position([0.5, -0.5, 4])
        geometry = BoxGeometry()
        # material = PointMaterial(property_dict={"baseColor": [1, 1, 0], "pointSize": 5})
        material = SurfaceMaterial(property_dict={"useVertexColors": True})
        # material = SurfaceMaterial(
        #     property_dict= {
        #         "useVertexColors": True,
        #         "wireframe": True,
        #         "lineWidth": 8
        #     }
        # )
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)
        self.rotationSpeed = 1.0
        self.accelaration = 1.0

    def update(self):
        self.mesh.rotate_y(0.02514 * self.rotationSpeed)
        self.mesh.rotate_x(0.01337 * self.rotationSpeed)
        self.renderer.render(self.scene, self.camera)
        if(self.input.is_key_down('s') and self.rotationSpeed != 0):
            self.rotationSpeed -= self.accelaration
        if(self.input.is_key_down('f')):
            self.rotationSpeed += self.accelaration



# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
