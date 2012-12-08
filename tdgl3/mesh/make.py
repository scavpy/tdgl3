"""

  Make various meshes

"""

from pyglet.gl import GL_QUADS, GL_TRIANGLES, GL_TRIANGLE_FAN
from tdgl3.mesh import tnvmesh



def cuboid(dx, dy, dz):
    """ make a TNVMesh with a single piece called "cuboid" made of GL_QUADS 
      centered on the origin, with width 2*dx, length 2*dy, height 2*dz.

      Texture coords 0 are scaled with the cuboid size
      Texture coords 1 are 0-1 on each face regardless of size
    """
    order = 'VNTU'
    vdata = [
    #Vx   Vy   Vz  Nx  Ny  Nz  Ts  Tt Us Ut
    -dx, -dy, -dz,  0, -1,  0, 0,   0, 0, 0, # front
     dx, -dy, -dz,  0, -1,  0, dx,  0, 1, 0,
     dx, -dy,  dz,  0, -1,  0, dx, dz, 1, 1,
    -dx, -dy,  dz,  0, -1,  0, 0,  dz, 0, 1,
     dx, -dy, -dz,  1,  0,  0, 0,   0, 0, 0, # right
     dx,  dy, -dz,  1,  0,  0, dy,  0, 1, 0,
     dx,  dy,  dz,  1,  0,  0, dy, dz, 1, 1,
     dx, -dy,  dz,  1,  0,  0, 0,  dz, 0, 1,
     dx,  dy, -dz,  0,  1,  0, 0,   0, 0, 0, # back
    -dx,  dy, -dz,  0,  1,  0, dx,  0, 1, 0,
    -dx,  dy,  dz,  0,  1,  0, dx, dz, 1, 1,
     dx,  dy,  dz,  0,  1,  0, 0,  dz, 0, 1,
    -dx,  dy, -dz, -1,  0,  0, 0,   0, 0, 0, # left
    -dx, -dy, -dz, -1,  0,  0, dy,  0, 1, 0,
    -dx, -dy,  dz, -1,  0,  0, dy, dz, 1, 1,
    -dx,  dy,  dz, -1,  0,  0, 0,  dz, 0, 1,
    -dx, -dy,  dz,  0,  0,  1, 0,   0, 0, 0, # top
     dx, -dy,  dz,  0,  0,  1, dx,  0, 1, 0,
     dx,  dy,  dz,  0,  0,  1, dx, dy, 1, 1,
    -dx,  dy,  dz,  0,  0,  1, 0,  dy, 0, 1,
    -dx,  dy, -dz,  0,  0, -1, 0,  0,  0, 0, # bottom
     dx,  dy, -dz,  0,  0, -1, dx, 0,  1, 0,
     dx, -dy, -dz,  0,  0, -1, dx, dy, 1, 1,
    -dx, -dy, -dz,  0,  0, -1, 0,  dy, 0, 1,
    ]
    quad_cuboid_piece = tnvmesh.TNVPiece(range(24), GL_QUADS)
    return tnvmesh.TNVMesh(vdata, order, dict(cuboid=quad_cuboid_piece))
