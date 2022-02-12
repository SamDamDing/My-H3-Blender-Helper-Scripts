"""
This script is for generating a grid of cubes with seams and skies. The triangulation modifers alternate every other cube so the seams line up.
Materials are created and applied to each cube. However, the perimeter cubes are not setup to be properly assigned materials unless the code is modified, which I haven't gotten around to yet.
This generates a 7x7 grid of cubes with skies on the outside, a ground texture on the bottom, and a seam mat in between. This code does not work for Halo 3, as the maximum amount of bsps connected to one is 2.
Hopefully this will increase as more mod tools are released.
"""
import bpy
import bmesh
bpy.context.scene.cursor.location[0] = 0
bpy.context.scene.cursor.location[1] = 0
bpy.context.scene.cursor.location[2] = 0
gridsizex=7
gridsizey=7
spacingX=45000
spacingY=45000
xlimit = gridsizex*spacingX-spacingX
ylimit = gridsizey*spacingY-spacingY
maxobj=gridsizex*gridsizey

def create_material(mat_name, diffuse_color=(1,1,1,1)):
    mat = bpy.data.materials.new(name=mat_name)
    mat.diffuse_color = diffuse_color
    return mat

def triangulate_fixed_object(obj):
    me = bpy.context.object.data
    bm = bmesh.new()
    bm.from_mesh(me)
    bmesh.ops.triangulate(
    bm,
    faces=bm.faces[:],
    quad_method='FIXED',
    ngon_method='BEAUTY')
    bm.to_mesh(me)
    bm.free()

def triangulate_fixed_alt_object(obj):
    me = bpy.context.object.data
    bm = bmesh.new()
    bm.from_mesh(me)
    bmesh.ops.triangulate(
    bm,
    faces=bm.faces[:],
    quad_method='ALTERNATE',
    ngon_method='BEAUTY')
    bm.to_mesh(me)
    bm.free()

def mat_set_sky(obj):
    me = bpy.context.object.data
    bm = bmesh.from_edit_mesh(me)
    bm.from_mesh(me)
    bm.faces.ensure_lookup_table()
    bm.faces[5].material_index = 1

def mat_set_sky_Y(obj):
    me = bpy.context.object.data
    bm = bmesh.from_edit_mesh(me)
    bm.from_mesh(me)
    bm.faces.ensure_lookup_table()
    bm.faces[1].material_index = 1

def mat_set_sky_YNeg(obj):
    me = bpy.context.object.data
    bm = bmesh.from_edit_mesh(me)
    bm.from_mesh(me)
    bm.faces.ensure_lookup_table()
    bm.faces[3].material_index = 1

def mat_set_sky_XNeg(obj):
    me = bpy.context.object.data
    bm = bmesh.from_edit_mesh(me)
    bm.from_mesh(me)
    bm.faces.ensure_lookup_table()
    bm.faces[0].material_index = 1

def mat_set_sky_X(obj):
    me = bpy.context.object.data
    bm = bmesh.from_edit_mesh(me)
    bm.from_mesh(me)
    bm.faces.ensure_lookup_table()
    bm.faces[2].material_index = 1

def mat_set_floor(obj):
    me = bpy.context.object.data
    bm = bmesh.from_edit_mesh(me)
    bm.from_mesh(me)
    bm.faces.ensure_lookup_table()
    bm.faces[4].material_index = 2

xrangeneg = range(1,49,7)
xrangepos = range(7,49,7)

i=1

while i <= maxobj:
    bpy.context.scene.cursor.location[0] = bpy.context.scene.cursor.location[0]+spacingX
    if i <= 1:
        bpy.context.scene.cursor.location[0] = 0
    if bpy.context.scene.cursor.location[0] > xlimit:
        bpy.context.scene.cursor.location[0] = 0
        bpy.context.scene.cursor.location[1] = bpy.context.scene.cursor.location[1]+spacingY
        
    #Makes the level_i box
    bpy.ops.mesh.primitive_cube_add(size=45000, enter_editmode=True, align='CURSOR')
    for obj in bpy.context.selected_objects:
        obj.name = "level_" + str(i)
        bsp = bpy.data.objects["level_" + str(i)]
        #bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.flip_normals()
        #bpy.ops.object.editmode_toggle()
        bpy.ops.object.material_slot_add()
        seammat = bpy.data.materials.new("+seam:" + str(i))
        seammat.diffuse_color = (.3,1,.8,1)
        bpy.context.object.active_material = seammat
        bpy.ops.object.material_slot_add()
        bpy.context.object.active_material = bpy.data.materials.new("+sky")
        bpy.context.object.active_material.diffuse_color = (0,0.15,1,1)
        bpy.ops.object.material_slot_add()
        bpy.context.object.active_material = bpy.data.materials.new("river ground_lake_deep")
        bpy.context.object.active_material.diffuse_color = (1,.15,0,1)
        print(bpy.context.active_object)
        
        #Sets the sky materials to faces depending on faces. Only want exteriors
        mat_set_floor(bpy.context.active_object)
        mat_set_sky(bpy.context.active_object)
        if 43 <= i <= 49:
            mat_set_sky_Y(bpy.context.active_object)
        if 1 <= i <= 7:
            mat_set_sky_YNeg(bpy.context.active_object)
        if i in xrangeneg:
            mat_set_sky_XNeg(bpy.context.active_object)
        if i in xrangepos:
            mat_set_sky_X(bpy.context.active_object)
            
        #Poking the mesh faces is easier than triangulation modifiers and gives the same effect.
        bpy.ops.mesh.poke()
        bpy.ops.object.mode_set(mode='OBJECT')
        
        """
        #Triangulation modifier
        if (i % 2) == 0:
            triangulate_fixed_object(bpy.context.active_object)
        else:
            triangulate_fixed_alt_object(bpy.context.active_object)
        """
        
    #Makes the shit in my ass. ASS NEEDS SHIT IN IT TO IMPORT
    bpy.ops.mesh.primitive_cube_add(size=2,align='CURSOR')
    for obj in bpy.context.selected_objects:
        obj.name = "poop_" + str(i)
        bpy.data.objects["level_"+ str(i)].select = False 
        bpy.data.objects["poop_"+ str(i)].select = True 
        bpy.ops.object.material_slot_add()
        #bpy.data.materials.new("river ground_lake_deep")
        bpy.context.object.active_material = bpy.data.materials.new("river ground_lake_deep")
        pooproot = bpy.data.objects["poop_"+ str(i)]
        bpy.ops.object.parent_set()

    #Makes the b_levelroot_i box
    bpy.ops.mesh.primitive_cube_add(size=2,align='CURSOR')
    for obj in bpy.context.selected_objects:
        obj.name = "b_levelroot_" + str(i)
        root = bpy.data.objects["b_levelroot_"+ str(i)]
        bpy.ops.object.parent_set()
        bpy.data.objects["level_"+ str(i)].parent = bpy.data.objects["b_levelroot_"+ str(i)]
        bpy.data.objects["level_"+ str(i)].matrix_parent_inverse = bpy.data.objects["b_levelroot_"+ str(i)].matrix_world.inverted()
        bpy.data.objects["poop_"+ str(i)].parent = bpy.data.objects["b_levelroot_"+ str(i)]
        bpy.data.objects["poop_"+ str(i)].matrix_parent_inverse = bpy.data.objects["b_levelroot_"+ str(i)].matrix_world.inverted()
        bpy.data.objects["b_levelroot_"+ str(i)].select = True  
        bpy.data.objects["level_"+ str(i)].select = True 
        bpy.data.objects["poop_"+ str(i)].select = True 
        print(bpy.context.selected_objects)
        #bpy.ops.collection.create(name='b_levelroot_' + str(i))
    print(i)
    i +=1

#Deletes any duplicate materials
mats = bpy.data.materials
for obj in bpy.data.objects:
    for slt in obj.material_slots:
        part = slt.name.rpartition('.')
        if part[2].isnumeric() and part[0] in mats:
            slt.material = mats.get(part[0])
