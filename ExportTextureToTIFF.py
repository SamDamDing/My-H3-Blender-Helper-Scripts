import bpy
#Exports Textures to TIFF
for obj in bpy.context.scene.objects:
    for s in obj.material_slots:
        if s.material and s.material.use_nodes:
            for n in s.material.node_tree.nodes:
                if n.type == 'TEX_IMAGE':
                    n.image.filepath_raw = "F:/SteamLibrary/steamapps/common/H3EK/tags/bitmaps/" + n.image.name + ".tif"
                    n.image.file_format = "TIFF"
                    n.image.save()
