import bpy
#Replaces any duplicate materials ending in .xxx with the original material, if available.
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
