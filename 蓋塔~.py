# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 11:18:19 2021

@author: freef
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x,y,z = mc.player.getTilePos()

while True:
    mc.setBlock(x,y,z,95,14)
    time.sleep(0.5)
    y=y+1
    mc.setBlock(x,y,z,95,1)
    time.sleep(0.5)
    y=y+1
    mc.setBlock(x,y,z,95,4)
    time.sleep(0.5)
    y=y+1
    mc.setBlock(x,y,z,95,5)
    time.sleep(0.5)
    y=y+1
    mc.setBlock(x,y,z,95,3)
    time.sleep(0.5)
    y=y+1
    mc.setBlock(x,y,z,95,11)
    time.sleep(0.5)
    y=y+1
    mc.setBlock(x,y,z,95,10)
    time.sleep(0.5)
    y=y+1