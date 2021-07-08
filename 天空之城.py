# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 09:59:26 2021

@author: freef
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
width = 10
height = 5
length = 6
blockType = 20
air= 0
mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType)
mc.setBlocks(x + 1, y + 1, z + 1,x + width - 1, y + height - 1, z + length - 1, air)
