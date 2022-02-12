import bpy
#Replaces any duplicate materials ending in .xxx with the original material, if available.
mats = bpy.data.materials
for obj in bpy.data.objects:
    for slt in obj.material_slots:
        part = slt.name.rpartition('.')
        if part[2].isnumeric() and part[0] in mats:
            slt.material = mats.get(part[0])
