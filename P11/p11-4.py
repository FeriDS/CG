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
from geometry.sphere import *
from geometry.rectangle import *
from geometry.tree import *
from geometry.castanets import *
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
        print("instrument selecter: 1(guitarra), 2(castanholas)")
        print("camera movement: WASDRF(move), QE(turn), RF(up and down),TG(look).")
        print("instrument movement: UHJKOL(move), YI(turn), OL(up and down), PÇ(look).")
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
        self.rig2.set_position([2, 0.8, -0.5])
        self.scene.add(self.rig2)


        # treeMain1_geometry = TreeMainBodyGeo()
        # treeMain1_material = TextureMaterial(texture=Texture(file_name="images/BarkDecidious0143_5_S.jpg"))
        # treeMain1 = Mesh(treeMain1_geometry, treeMain1_material)
        # self.scene.add(treeMain1)

        castanets_geometry_up = CastanetsGeometryUp()
        castanets_material_up = TextureMaterial(texture=Texture(file_name="images/wood_texture_2.jpg"))
        self.castanets_up = Mesh(castanets_geometry_up, castanets_material_up)
        castanets_geometry_down = CastanetsGeometryDown()
        castanets_material_down = TextureMaterial(texture=Texture(file_name="images/wood_texture.jpg"))
        self.castanets_down = Mesh(castanets_geometry_down, castanets_material_down)
        self.rig3 = MovementRig2()
        self.rig3.add(self.castanets_up)
        self.rig3.add(self.castanets_down)
        self.rig3.set_position([-2, 0.8, -0.5])
        self.scene.add(self.rig3)


        axes = AxesHelper(axis_length=2)
        self.scene.add(axes)
        grid = GridHelper(
            size=20,
            grid_color=[1, 1, 1],
            center_color=[1, 1, 0]
        )
        grid.rotate_x(-math.pi / 2)
        self.scene.add(grid)



        sky_geometry = SphereGeometry(radius=50)
        sky_material = TextureMaterial(texture=Texture(file_name="images/sky.jpg"))
        sky = Mesh(sky_geometry, sky_material)
        self.scene.add(sky)
        grass_geometry = RectangleGeometry(width=100, height=100)
        grass_material = TextureMaterial(
            texture=Texture(file_name="images/grass.jpg"),
            property_dict={"repeatUV": [50, 50]}
        )
        grass = Mesh(grass_geometry, grass_material)
        grass.rotate_x(-math.pi/2)
        self.scene.add(grass)
        self.bool = True

    def update(self):
        if self.input.is_key_pressed("1"):
            self.bool = True
        if self.input.is_key_pressed("2"):
            self.bool = False
        if self.bool:
            self.rig2.update(self.input, self.delta_time)
        else:
            self.rig3.update(self.input, self.delta_time)
        self.rig1.update(self.input, self.delta_time)
        self.renderer.render(self.scene, self.camera)


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
