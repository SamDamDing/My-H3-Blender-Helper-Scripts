bl_info = {
    "name": "Halo Material Tools",
    "author": "MercyMoon",
    "version": (0, 1),
    "blender": (3, 0, 0),
    "category": "3D View"
}

import os
import bpy
from bpy_extras.io_utils import ExportHelper

class MyAddonProperties(bpy.types.PropertyGroup):
    some_integer_prop = bpy.props.IntProperty()
    some_identifier: bpy.props.StringProperty(
        name='Directory',
        description='Directory')

class WMFileRemover(bpy.types.Operator):
    bl_idname = "wm.remove_file"
    bl_label = "Remove File"
    def execute(self, context):
        fp = context.scene.my_addon.some_identifier
        if fp:
            print('os.remove(', fp, ')')
            os.remove(fp)
        else:
            self.report({'ERROR'}, 'filepath is an empty string')
        return {'FINISHED'}

class WMFileSelector(bpy.types.Operator, ExportHelper):
    bl_idname = "halomats.identifier_selector"
    bl_label = "some folder"
    bl_description = 'Directory'
    filename_ext = ""
    def execute(self, context):
        fdir = self.properties.filepath
        context.scene.my_addon.some_identifier = fdir
        return{'FINISHED'}

class EnableHaloMatProp(bpy.types.Operator):
    bl_idname = 'halomats.enablehalomatprop'
    bl_label = 'Toggle Properties'
    bl_description = 'Enable or Disable Halo Material Properties'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    if mat.ass_jms.is_bm == False:
                        mat.ass_jms.is_bm = True
                    else:
                        mat.ass_jms.is_bm = False
        return {"FINISHED"}


class renderOnly(bpy.types.Operator):
    bl_idname = 'halomats.renderonly'
    bl_label = 'Render Only'
    bl_description = 'Makes the material Render Only'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.render_only == False:
                        mat.ass_jms.render_only = True
                    else:
                        mat.ass_jms.render_only = False
        return {"FINISHED"}
    
class TwoSided(bpy.types.Operator):
    bl_idname = 'halomats.twosided'
    bl_label = 'TwoSided'
    bl_description = 'Makes the material Two Sided'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.two_sided == False:
                        mat.ass_jms.two_sided = True
                    else:
                        mat.ass_jms.two_sided = False
        return {"FINISHED"}

class Transparent(bpy.types.Operator):
    bl_idname = 'halomats.transparent'
    bl_label = 'Transparent'
    bl_description = 'Makes the material Transparent'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.transparent_1_sided == False:
                        mat.ass_jms.transparent_1_sided = True
                    else:
                        mat.ass_jms.transparent_1_sided = False
                        
        return {"FINISHED"}

class LargeCollideable(bpy.types.Operator):
    bl_idname = 'halomats.largecollideable'
    bl_label = 'LargeCollideable'
    bl_description = 'Makes the material a Large Collideable'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.sphere_collision_only == False:
                        mat.ass_jms.sphere_collision_only = True
                    else:
                        mat.ass_jms.sphere_collision_only = False
        return {"FINISHED"}

class FogPlane(bpy.types.Operator):
    bl_idname = 'halomats.fogplane'
    bl_label = 'FogPlane'
    bl_description = 'Makes the material a Fog Plane'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.fog_plane == False:
                        mat.ass_jms.fog_plane = True
                    else:
                        mat.ass_jms.fog_plane = False
        return {"FINISHED"}

class Ladder(bpy.types.Operator):
    bl_idname = 'halomats.ladder'
    bl_label = 'ladder'
    bl_description = 'Makes the material a Ladder'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.ladder == False:
                        mat.ass_jms.ladder = True
                    else:
                        mat.ass_jms.ladder = False
        return {"FINISHED"}

class collision_only(bpy.types.Operator):
    bl_idname = 'halomats.collision_only'
    bl_label = 'collision_only'
    bl_description = 'Makes the material Collision Only'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.collision_only == False:
                        mat.ass_jms.collision_only = True
                    else:
                        mat.ass_jms.collision_only = False
        return {"FINISHED"}

class breakable(bpy.types.Operator):
    bl_idname = 'halomats.breakable'
    bl_label = 'breakable'
    bl_description = 'Makes the material Breakable'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.breakable == False:
                        mat.ass_jms.breakable = True
                    else:
                        mat.ass_jms.breakable = False
        return {"FINISHED"}

class ai_deafening(bpy.types.Operator):
    bl_idname = 'halomats.ai_deafening'
    bl_label = 'ai_deafening'
    bl_description = 'Makes the material a Fog Plane'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.ai_deafening == False:
                        mat.ass_jms.ai_deafening = True
                    else:
                        mat.ass_jms.ai_deafening = False
        return {"FINISHED"}

class portal_exact(bpy.types.Operator):
    bl_idname = 'halomats.portal_exact'
    bl_label = 'portal_exact'
    bl_description = 'Makes the material an Exact Portal'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.portal_exact == False:
                        mat.ass_jms.portal_exact = True
                    else:
                        mat.ass_jms.portal_exact = False
        return {"FINISHED"}


class makeDupesInstance(bpy.types.Operator):
    bl_idname = 'halomats.makedupesinstance'
    bl_label = 'Make Dupes Instances'
    bl_description = 'Replaces any duplicate objects ending in .xxx with an instanced object, if possible.'
    def execute(self, context):
        objs = bpy.data.objects
        for obj in bpy.data.objects:
            part = obj.name.rpartition('.')
            if part[2].isnumeric() and part[0] in objs:
                print(obj.name)
                obj.name = '%' + str(obj.name)
        return {"FINISHED"}

class removeDupeMats(bpy.types.Operator):
    bl_idname = 'halomats.removedupemats'
    bl_label = 'Remove Material Duplicates'
    bl_description = 'Replaces any duplicate materials ending in .xxx with the original material, if available.'
    def execute(self, context):
        mats = bpy.data.materials
        for obj in bpy.data.objects:
            for s in obj.material_slots:
                if s.material and s.material.use_nodes:
                    for n in s.material.node_tree.nodes:
                        if n.type == 'TEX_IMAGE':
                            #texture_list += [n.image]
                            imagename=n.image.name
                            part = s.name.rpartition('.')
                            if part[2].isnumeric() and part[0] in mats:
                                ogmat=mats.get(part[0])
                                for ogs in ogmat.node_tree.nodes:
                                    if ogs.type=='TEX_IMAGE':
                                        ogimg=ogs.image.name
                                        if ogimg==imagename:
                                            s.material = ogmat
class ExportTexture(bpy.types.Operator):
    bl_idname = 'halomats.exporttexture'
    bl_label = 'Export Material Textures to tiff'
    bl_description = 'Export Material Textures to the directory in a TIFF format'
    def execute(self, context):
        scn = context.scene
        for obj in bpy.context.scene.objects:
            for s in obj.material_slots:
                if s.material and s.material.use_nodes:
                    for n in s.material.node_tree.nodes:
                        if n.type == 'TEX_IMAGE':
                            imagename=n.image.name
                            imagename = imagename.rpartition('.')
                            imagename = imagename[0]
                            print(imagename)
                            n.image.filepath_raw = str(scn.my_addon.some_identifier + str(imagename) + ".tif")
                            print(n.image.filepath_raw)
                            n.image.file_format = "TIFF"
                            n.image.save()
        return {"FINISHED"}

class PANEL1(bpy.types.Panel):
    bl_idname = "WMFILEPANEL_PT_hello"
    bl_label = "Halo Material Tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Halo Material Tools"
    def draw(self, context):
        layout = self.layout
        scn = context.scene
        col = layout.column()
        row = col.row(align=True)
        row.prop(scn.my_addon, 'some_identifier', text="")
        col.operator("halomats.identifier_selector", icon="FILE_FOLDER", text="Directory")
        row = col.row(align=True)
        row.operator("halomats.enablehalomatprop", icon='SHADERFX', text="Toggle Material Properties")
        row = col.row(align=True)
        row.operator("halomats.twosided", icon='MATERIAL', text="Two-Sided")
        row = col.row(align=True)
        row.operator("halomats.transparent", icon='MATERIAL', text="Transparent")
        row = col.row(align=True)
        row.operator("halomats.renderonly", icon='MATERIAL', text="Render Only")
        row = col.row(align=True)
        row.operator("halomats.largecollideable", icon='MATERIAL', text="Large Collideable")
        row = col.row(align=True)
        row.operator("halomats.fogplane", icon='MATERIAL', text="Fog Plane")
        row = col.row(align=True)
        row.operator("halomats.ladder", icon='MATERIAL', text="Ladder")
        row = col.row(align=True)
        row.operator("halomats.breakable", icon='MATERIAL', text="Breakable")
        row = col.row(align=True)
        row.operator("halomats.ai_deafening", icon='MATERIAL', text="AI Deafening")
        row = col.row(align=True)
        row.operator("halomats.collision_only", icon='MATERIAL', text="Collision Only")
        row = col.row(align=True)
        row.operator("halomats.portal_exact", icon='MATERIAL', text="Exact Portal")
        col = layout.column()
        col.operator("halomats.removedupemats", icon='REMOVE', text="Remove Dupe Materials")
        col = layout.column()
        col.operator("halomats.makedupesinstance", icon='COLLECTION_NEW', text="Make Dupes Instances")
        col = layout.column()
        col.operator("halomats.exporttexture", icon='TEXTURE', text="Export Textures")

def register():
    bpy.utils.register_class(PANEL1)
    bpy.utils.register_class(MyAddonProperties)
    bpy.types.Scene.my_addon = bpy.props.PointerProperty(type=MyAddonProperties)
    bpy.utils.register_class(WMFileRemover)
    bpy.utils.register_class(WMFileSelector)
    bpy.utils.register_class(renderOnly)
    bpy.utils.register_class(TwoSided)
    bpy.utils.register_class(Transparent)
    bpy.utils.register_class(LargeCollideable)
    bpy.utils.register_class(FogPlane)
    bpy.utils.register_class(Ladder)
    bpy.utils.register_class(collision_only)
    bpy.utils.register_class(breakable)
    bpy.utils.register_class(ai_deafening)
    bpy.utils.register_class(portal_exact)
    bpy.utils.register_class(EnableHaloMatProp)
    bpy.utils.register_class(makeDupesInstance)
    bpy.utils.register_class(removeDupeMats)
    bpy.utils.register_class(ExportTexture)
    
def unregister():
    bpy.utils.unregister_class(PANEL1)
    bpy.utils.unregister_class(MyAddonProperties)
    bpy.utils.unregister_class(WMFileRemover)
    bpy.utils.unregister_class(WMFileSelector)
    bpy.utils.unregister_class(renderOnly)
    bpy.utils.unregister_class(TwoSided)
    bpy.utils.unregister_class(Transparent)
    bpy.utils.unregister_class(LargeCollideable)
    bpy.utils.unregister_class(FogPlane)
    bpy.utils.unregister_class(Ladder)
    bpy.utils.unregister_class(collision_only)
    bpy.utils.unregister_class(breakable)
    bpy.utils.unregister_class(ai_deafening)
    bpy.utils.unregister_class(portal_exact)
    bpy.utils.unregister_class(EnableHaloMatProp)
    bpy.utils.unregister_class(makeDupesInstance)
    bpy.utils.unregister_class(removeDupeMats)
    bpy.utils.unregister_class(ExportTexture)
    del bpy.types.Scene.my_addon

if __name__ == "__main__" :
    register()
