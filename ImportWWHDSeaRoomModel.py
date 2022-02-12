import bpy
spacingX=100000
spacingY=100000
maxobj=49
#Grid Top Left
tl=-300000
xrange = range(1,49,7)
i=1
xpos=-300000
ypos=400000
while i <=49:
    path = "I:\\Wind Waker HD Dumped\\content\\Common\\Stage\\sea_Room" + str(i) + "\\Room" + str(i) +"\\model.dae"
    bpy.ops.wm.collada_import(filepath = path, 
                      auto_connect = True, 
                      find_chains = True, 
                      fix_orientation = True)
    if i in xrange:
        xpos = tl
        ypos = ypos-spacingY
    bpy.ops.transform.translate(
    value=(xpos, ypos, 0), 
    orient_axis_ortho='X', 
    orient_type='GLOBAL', 
    orient_matrix=(
    (1, 0, 0), 
    (0, 1, 0), 
    (0, 0, 1)), 
    orient_matrix_type='GLOBAL', 
    constraint_axis=(True, False, False), 
    mirror=False, 
    use_proportional_edit=False, 
    proportional_edit_falloff='SMOOTH', 
    proportional_size=1, 
    use_proportional_connected=False, 
    use_proportional_projected=False, 
    release_confirm=True)
    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
    xpos=xpos+spacingX
    i +=1
