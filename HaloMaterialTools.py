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
import subprocess
import sys

class ToolCmd(bpy.types.Operator):
    bl_idname = 'halomats.toolcmd'
    bl_label = 'Tool CMD'
    bl_description = 'Tool CMD'
    def execute(self, context):
        print("Start")
        scn = context.scene
        H3EK = str(scn.my_addon.some_identifier)
        print("H3EK Path: " + H3EK)
        Tool = H3EK + r'\tool.exe'
        print("Tool Path: " + Tool)
        BitmapPath = str(scn.my_addon.data_identifier)
        BitmapPath = str(BitmapPath.split(H3EK)[1])
        BitmapPath = str(BitmapPath.split("data\\")[1])
        print("Bitmap Path: " + BitmapPath)
        result = subprocess.Popen([Tool, "bitmaps", BitmapPath], cwd=H3EK)
        print("stdout:", result.stdout)
        return {'FINISHED'}

class MyAddonProperties(bpy.types.PropertyGroup):
    some_integer_prop = bpy.props.IntProperty()
    some_identifier: bpy.props.StringProperty(
        name='Directory',
        description='Directory')
    data_identifier: bpy.props.StringProperty(
        name='DataDirectory',
        description='DataDirectory')    

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

class DataPathFileSelector(bpy.types.Operator, ExportHelper):
    bl_idname = "halomats.data_path_identifier_selector"
    bl_label = "Data Folder"
    bl_description = 'H3EK Data Directory'
    filename_ext = ""
    def execute(self, context):
        fdatadir = self.properties.filepath
        context.scene.my_addon.data_identifier = fdatadir
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

class no_shadow(bpy.types.Operator):
    bl_idname = 'halomats.no_shadow'
    bl_label = 'no_shadow'
    bl_description = 'Makes the material no_shadow'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.no_shadow == False:
                        mat.ass_jms.no_shadow = True
                    else:
                        mat.ass_jms.no_shadow = False
        return {"FINISHED"}

class shadow_only(bpy.types.Operator):
    bl_idname = 'halomats.shadow_only'
    bl_label = 'shadow_only'
    bl_description = 'Makes the material shadow_only'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.shadow_only == False:
                        mat.ass_jms.shadow_only = True
                    else:
                        mat.ass_jms.shadow_only = False
        return {"FINISHED"}

class lightmap_only(bpy.types.Operator):
    bl_idname = 'halomats.lightmap_only'
    bl_label = 'lightmap_only'
    bl_description = 'Makes the material lightmap_only'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.lightmap_only == False:
                        mat.ass_jms.lightmap_only = True
                    else:
                        mat.ass_jms.lightmap_only = False
        return {"FINISHED"}

class precise(bpy.types.Operator):
    bl_idname = 'halomats.precise'
    bl_label = 'precise'
    bl_description = 'Makes the material precise'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.precise == False:
                        mat.ass_jms.precise = True
                    else:
                        mat.ass_jms.precise = False
        return {"FINISHED"}

class conveyor(bpy.types.Operator):
    bl_idname = 'halomats.conveyor'
    bl_label = 'conveyor'
    bl_description = 'Makes the material conveyor'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.conveyor == False:
                        mat.ass_jms.conveyor = True
                    else:
                        mat.ass_jms.conveyor = False
        return {"FINISHED"}

class portal_1_way(bpy.types.Operator):
    bl_idname = 'halomats.portal_1_way'
    bl_label = 'portal_1_way'
    bl_description = 'Makes the material portal_1_way'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.portal_1_way == False:
                        mat.ass_jms.portal_1_way = True
                    else:
                        mat.ass_jms.portal_1_way = False
        return {"FINISHED"}

class portal_door(bpy.types.Operator):
    bl_idname = 'halomats.portal_door'
    bl_label = 'portal_door'
    bl_description = 'Makes the material portal_door'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.portal_door == False:
                        mat.ass_jms.portal_door = True
                    else:
                        mat.ass_jms.portal_door = False
        return {"FINISHED"}

class portal_vis_blocker(bpy.types.Operator):
    bl_idname = 'halomats.portal_vis_blocker'
    bl_label = 'portal_vis_blocker'
    bl_description = 'Makes the material portal_vis_blocker'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.portal_vis_blocker == False:
                        mat.ass_jms.portal_vis_blocker = True
                    else:
                        mat.ass_jms.portal_vis_blocker = False
        return {"FINISHED"}

class ignored_by_lightmaps(bpy.types.Operator):
    bl_idname = 'halomats.ignored_by_lightmaps'
    bl_label = 'ignored_by_lightmaps'
    bl_description = 'Makes the material ignored_by_lightmaps'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.ignored_by_lightmaps == False:
                        mat.ass_jms.ignored_by_lightmaps = True
                    else:
                        mat.ass_jms.ignored_by_lightmaps = False
        return {"FINISHED"}

class blocks_sound(bpy.types.Operator):
    bl_idname = 'halomats.blocks_sound'
    bl_label = 'blocks_sound'
    bl_description = 'Makes the material blocks_sound'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.blocks_sound == False:
                        mat.ass_jms.blocks_sound = True
                    else:
                        mat.ass_jms.blocks_sound = False
        return {"FINISHED"}

class decal_offset(bpy.types.Operator):
    bl_idname = 'halomats.decal_offset'
    bl_label = 'decal_offset'
    bl_description = 'Makes the material decal_offset'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.decal_offset == False:
                        mat.ass_jms.decal_offset = True
                    else:
                        mat.ass_jms.decal_offset = False
        return {"FINISHED"}

class water_surface(bpy.types.Operator):
    bl_idname = 'halomats.water_surface'
    bl_label = 'water_surface'
    bl_description = 'Makes the material water_surface'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.water_surface == False:
                        mat.ass_jms.water_surface = True
                    else:
                        mat.ass_jms.water_surface = False
        return {"FINISHED"}

class slip_surface(bpy.types.Operator):
    bl_idname = 'halomats.slip_surface'
    bl_label = 'slip_surface'
    bl_description = 'Makes the material slip_surface'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.slip_surface == False:
                        mat.ass_jms.slip_surface = True
                    else:
                        mat.ass_jms.slip_surface = False
        return {"FINISHED"}

class group_transparents_by_plane(bpy.types.Operator):
    bl_idname = 'halomats.group_transparents_by_plane'
    bl_label = 'group_transparents_by_plane'
    bl_description = 'Makes the material group_transparents_by_plane'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.group_transparents_by_plane == False:
                        mat.ass_jms.group_transparents_by_plane = True
                    else:
                        mat.ass_jms.group_transparents_by_plane = False
        return {"FINISHED"}

class transparent_2_sided(bpy.types.Operator):
    bl_idname = 'halomats.transparent_2_sided'
    bl_label = 'transparent_2_sided'
    bl_description = 'Makes the material transparent_2_sided'
    def execute(self, context):
        for object in bpy.context.selected_objects: 
            if object.type in {'MESH','CURVE', 'SURFACE','META', 'FONT'}:
                for mat in bpy.data.materials:
                    mat.ass_jms.is_bm = True
                    if mat.ass_jms.transparent_2_sided == False:
                        mat.ass_jms.transparent_2_sided = True
                    else:
                        mat.ass_jms.transparent_2_sided = False
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
        return {"FINISHED"}

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
                            n.image.filepath_raw = str(scn.my_addon.data_identifier + str(imagename) + ".tif")
                            print("Exporting " + n.image.name + " to " + n.image.filepath_raw)
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
        col = layout.column_flow(columns=1, align=True)
        row = col.row(align=True)
        col.prop(scn.my_addon, 'some_identifier', text="H3EK Directory")
        col.operator("halomats.identifier_selector", icon="FILE_FOLDER", text="Set H3EK Directory")
        col.prop(scn.my_addon, 'data_identifier', text="Data Directory")
        col.operator("halomats.data_path_identifier_selector", icon="FILE_FOLDER", text="Set Working Data Directory")
        col.operator("halomats.exporttexture", icon='TEXTURE', text="Export Textures")
        col.operator("halomats.toolcmd", icon='TEXTURE', text="Make Bitmaps")
        col.operator("halomats.removedupemats", icon='REMOVE', text="Remove Duplicate Materials")
        col.operator("halomats.makedupesinstance", icon='COLLECTION_NEW', text="Make Duplicates Instances")
        col = layout.column()
        col.operator("halomats.enablehalomatprop", icon='SHADERFX', text="Toggle Material Properties")
        row = col.grid_flow(row_major=True, columns=2, even_columns=True, even_rows=True, align=True)
        layout.ui_units_x=20
        row.operator("halomats.transparent_2_sided", icon='MATERIAL', text="Transparent 2 Sided")
        row.operator("halomats.transparent", icon='MATERIAL', text="Transparent")
        row.operator("halomats.renderonly", icon='MATERIAL', text="Render Only")
        row.operator("halomats.collision_only", icon='MATERIAL', text="Collision Only")
        row.operator("halomats.twosided", icon='MATERIAL', text="Two-Sided")
        row.operator("halomats.group_transparents_by_plane", icon='MATERIAL', text="Group Transparents By Plane")
        row.operator("halomats.largecollideable", icon='MATERIAL', text="Large Collideable")
        row.operator("halomats.fogplane", icon='MATERIAL', text="Fog Plane")
        row.operator("halomats.ladder", icon='MATERIAL', text="Ladder")
        row.operator("halomats.conveyor", icon='MATERIAL', text="Conveyor")
        row.operator("halomats.breakable", icon='MATERIAL', text="Breakable")
        row.operator("halomats.ai_deafening", icon='MATERIAL', text="AI Deafening")
        row.operator("halomats.no_shadow", icon='MATERIAL', text="No Shadow")
        row.operator("halomats.shadow_only", icon='MATERIAL', text="Shadow Only")
        row.operator("halomats.lightmap_only", icon='MATERIAL', text="Lightmap Only")
        row.operator("halomats.precise", icon='MATERIAL', text="Precise")
        row.operator("halomats.portal_exact", icon='MATERIAL', text="Exact Portal")
        row.operator("halomats.portal_1_way", icon='MATERIAL', text="Portal 1 Way")
        row.operator("halomats.portal_vis_blocker", icon='MATERIAL', text="Portal Vis Blocker")
        row.operator("halomats.ignored_by_lightmaps", icon='MATERIAL', text="Ignored By Lightmaps")
        row.operator("halomats.blocks_sound", icon='MATERIAL', text="Blocks Sound")
        row.operator("halomats.decal_offset", icon='MATERIAL', text="Decal Offset")
        row.operator("halomats.water_surface", icon='MATERIAL', text="Water Surface")
        row.operator("halomats.slip_surface", icon='MATERIAL', text="Slip Surface")

def register():
    bpy.utils.register_class(PANEL1)
    bpy.utils.register_class(MyAddonProperties)
    bpy.types.Scene.my_addon = bpy.props.PointerProperty(type=MyAddonProperties)
    bpy.utils.register_class(WMFileRemover)
    bpy.utils.register_class(WMFileSelector)
    bpy.utils.register_class(DataPathFileSelector)
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
    bpy.utils.register_class(ToolCmd)
    bpy.utils.register_class(no_shadow)
    bpy.utils.register_class(shadow_only)
    bpy.utils.register_class(lightmap_only)
    bpy.utils.register_class(precise)
    bpy.utils.register_class(conveyor)
    bpy.utils.register_class(portal_1_way)
    bpy.utils.register_class(portal_door)
    bpy.utils.register_class(portal_vis_blocker)
    bpy.utils.register_class(ignored_by_lightmaps)
    bpy.utils.register_class(blocks_sound)
    bpy.utils.register_class(decal_offset)
    bpy.utils.register_class(water_surface)
    bpy.utils.register_class(slip_surface)
    bpy.utils.register_class(group_transparents_by_plane)
    bpy.utils.register_class(transparent_2_sided)
    
def unregister():
    bpy.utils.unregister_class(PANEL1)
    bpy.utils.unregister_class(MyAddonProperties)
    bpy.utils.unregister_class(WMFileRemover)
    bpy.utils.unregister_class(WMFileSelector)
    bpy.utils.unregister_class(DataPathFileSelector)
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
    bpy.utils.unregister_class(ToolCmd)
    bpy.utils.unregister_class(no_shadow)
    bpy.utils.unregister_class(shadow_only)
    bpy.utils.unregister_class(lightmap_only)
    bpy.utils.unregister_class(precise)
    bpy.utils.unregister_class(conveyor)
    bpy.utils.unregister_class(portal_1_way)
    bpy.utils.unregister_class(portal_door)
    bpy.utils.unregister_class(portal_vis_blocker)
    bpy.utils.unregister_class(ignored_by_lightmaps)
    bpy.utils.unregister_class(blocks_sound)
    bpy.utils.unregister_class(decal_offset)
    bpy.utils.unregister_class(water_surface)
    bpy.utils.unregister_class(slip_surface)
    bpy.utils.unregister_class(group_transparents_by_plane)
    bpy.utils.unregister_class(transparent_2_sided)
    del bpy.types.Scene.my_addon

if __name__ == "__main__" :
    register()
