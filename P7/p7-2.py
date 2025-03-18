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
        self.camera.set_position([0, 0, 4])
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
        self.rotationSpeedY = 0.09
        self.accelaration = 0.2
        self.rotationSpeedX = 0.09
        self.rotationSpeedZ = 0.09
        self.rotateX = False
        self.rotateY = False
        self.rotateZ = False

    def update(self):
        if(self.input.is_key_down('s')):
            self.rotationSpeedZ -= self.accelaration
            self.rotationSpeedX -= self.accelaration
            self.rotationSpeedY -= self.accelaration
        if(self.input.is_key_down('f')):
            self.rotationSpeedX += self.accelaration
            self.rotationSpeedY += self.accelaration
            self.rotationSpeedZ += self.accelaration
        if(self.rotationSpeedX < 0):
            self.rotationSpeedX = 0
        if(self.rotationSpeedY < 0):
            self.rotationSpeedY = 0
        if(self.rotationSpeedZ < 0):
            self.rotationSpeedZ = 0
        if(self.input.is_key_down('x')):
            self.rotateX = not self.rotateX
        if(self.input.is_key_down('y')):
            self.rotateY = not self.rotateY
        if(self.input.is_key_down('z')):
            self.rotateZ = not self.rotateZ

        if self.rotateX:
            self.mesh.rotate_x(self.rotationSpeedX, False)
        if self.rotateY:
            self.mesh.rotate_y(self.rotationSpeedY, False)
        if self.rotateZ:
            self.mesh.rotate_z(self.rotationSpeedZ, False)
        self.renderer.render(self.scene, self.camera)



# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
