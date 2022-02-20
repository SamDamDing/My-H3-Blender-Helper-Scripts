#This makes all the objects selected render only and non collidable
import bpy
def render_only():
  for object in bpy.context.selected_objects: 
    if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
        for mat in bpy.data.materials:
            mat.ass_jms.is_bm = True
            mat.ass_jms.render_only = True
