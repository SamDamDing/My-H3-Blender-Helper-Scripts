import bpy
import os
from bpy import context
from bpy import data

C = bpy.context
count_replaced_files = 0
# Iterate through all objects in selection
for ob in C.selected_objects:
    if ob.type not in ('LIGHTS', 'CAMERA', 'VOLUME'): # OPTIONAL
        for slot in ob.material_slots:
            if slot.material is not None:
                old_name = slot.material.name
                # Get its first material slot
                material = slot.material
                # Get the nodes in the node tree
                nodes = material.node_tree.nodes
                # Get a principled node
                principled = next(n for n in nodes if n.type == 'BSDF_PRINCIPLED')
                # Get the slot for 'base color'
                base_color = principled.inputs['Base Color'] #Or principled.inputs[0]
                # Get the link
                link = base_color.links[0]
                link_node = link.from_node
                # Rename the material to the image name excluding the extension
                material.name = os.path.splitext( link_node.image.name )[0]
                # Print the results
                print( "Material Old Name:", old_name, )
                print( "Material New Name:", material.name )
                count_replaced_files += 1
print(str(count_replaced_files))
print('File were replaced')
