# tdgl3

Python 3 library based on Pyglet, for making simple 3D games


## project history

The tdgl library on sourceforge became too unwieldy and needed a redesign. I decided to do this as soon
as  Pyglet could do GLSL and run on Python 3.  With Pyglet 1.2 this is becoming true.

## road map

The redesign will happen incrementally, driven by the development of a game I've wanted to write for a
while now. Essentially, I am ditching everything that depends on the old OpenGL standard pipeline, and
will probably take apart the deeply-nested Part/Group hierarchy,  perhaps making the library more like
an entity/component system.

Nothing to see here yet, unfortunately.