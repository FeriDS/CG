import numpy as np
import math
import pathlib
import sys

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from geometry.guitarra import *
from core_ext.texture import Texture
from material.texture import TextureMaterial
from extras.axes import AxesHelper
from extras.grid import GridHelper
from extras.movement_rig1 import MovementRig1
from extras.movement_rig2 import MovementRig2


class Example(Base):
    """
    Render the axes and the rotated xy-grid.
    Add camera movement: WASDRF(move), QE(turn), RF(up and down),TG(look).
    Add box movement: UHJKOL(move), YI(turn), OL(up and down), PÇ(look).
    """
    def initialize(self):
        print("Initializing program...")
        print("camera movement: WASDRF(move), QE(turn), RF(up and down),TG(look).")
        print("box movement: UHJKOL(move), YI(turn), OL(up and down), PÇ(look).")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.rig1 = MovementRig1()
        self.rig1.add(self.camera)
        self.rig1.set_position([0.5, 1, 5])
        self.scene.add(self.rig1)

        guitarra_mainBody_geometry = GuitarraMainBodyGeo()
        guitarra_mainBody_material = TextureMaterial(texture=Texture(file_name="images/lightWood.png"))
        self.guitarra_mainBody = Mesh(guitarra_mainBody_geometry, guitarra_mainBody_material)
        self.rig2 = MovementRig2()
        self.rig2.add(self.guitarra_mainBody)

        guitarraStrings_geometry = GuitarraStringsGeo()
        guitarraStrings_material = TextureMaterial(texture=Texture(file_name="images/white.jpg"))
        self.guitarraStrings = Mesh(guitarraStrings_geometry, guitarraStrings_material)
        self.rig2.add(self.guitarraStrings)

        guitarraBlackParts_geometry = GuitarraBlackPartsAndMoreGeo()
        guitarraBlackParts_material = TextureMaterial(texture=Texture(file_name="images/darkWood.jpg"))
        self.guitarraBlackParts = Mesh(guitarraBlackParts_geometry, guitarraBlackParts_material)
        self.rig2.add(self.guitarraBlackParts)
        self.rig2.rotate_y(-math.pi/2)
        self.rig2.set_position([0, 0.5, -0.5])
        self.scene.add(self.rig2)

        axes = AxesHelper(axis_length=2)
        self.scene.add(axes)
        grid = GridHelper(
            size=20,
            grid_color=[1, 1, 1],
            center_color=[1, 1, 0]
        )
        grid.rotate_x(-math.pi / 2)
        self.scene.add(grid)

    def update(self):
        self.rig1.update(self.input, self.delta_time)
        self.rig2.update(self.input, self.delta_time)
        self.renderer.render(self.scene, self.camera)


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
