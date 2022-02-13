import bpy
import os
#This is some hacky ass shit so brace yourselves. I'm a dumbass who's too lazy to figure out proper structs and likes doing things the hard way, so the following is a hacky ass solution to a stupid ass problem.
#This script takes your objects in a scene, gets their materials textures, renames them to be 40 characters long as specified in the neededlength variable, then exports them to a folder specified by n.image.filepath_raw
#If that folder does not exist, change it to somewhere that does. Seriously, who keeps their H3EK shit on an F drive like I do?
#Anyway, those Tifs are generated there and then the material for the object is renamed to the name of that texture that was just renamed. Why? It's hacky bitswapping shit.
#If you were to generate bitmaps from these Tifs outright, Tool wouldn't like that, so I use my Gimp to convert them into a proper TIFF using the Batch Image Manipulation addon https://alessandrofrancesconi.it/projects/bimp/
#The output for proper tifs should be in your data/objects/bitmaps/custom directory. Don't have it? Make one.
#You can now have tool make bitmaps from those tiffs that will end up in your tags/objects/bitmaps/custom directory.
#Export your blender file as an fbx
#Use my fork of blader to generate shaders to your directory
#Modify the default_directory variable in the "H3ShaderBitmapTool Modify and Run 3rd.py" script to the directory you have your blader generated shaders in and run it.
#It'll probably fuck up a few of them because this script is a bit ass tbh. Like, it doesn't check for it duplicates. I'll probably get around to fixing it, but if that happens you'll have shaders with an invalid texture that looks red and rainbow.
#Finally, you can import your ass and hopefully your textures will look right.

texture_list = []
count_replaced_files = 0

for obj in bpy.context.scene.objects:
    for s in obj.material_slots:
        if s.material and s.material.use_nodes:
            for n in s.material.node_tree.nodes:
                if n.type == 'TEX_IMAGE':
                    texture_list += [n.image]
                    imagename=n.image.name
                    namelength=len(n.image.name)
                    neededlength = 40
                    longerlength = neededlength - namelength
                    console = "{3} is {0} characters long and needs to be {1} which is {2} characters longer"
                    if namelength < neededlength:
                        print(console.format(namelength, neededlength, longerlength, n.image.name))
                        count_replaced_files += 1
                        old_name = n.image.name
                        new_name = n.image.name
                        new_name = new_name.rjust(neededlength, '_')
                        n.image.name = new_name
                        info_string = old_name + ' has been replaced with ' + new_name
                        print(info_string)
                    if namelength > neededlength:
                        print(console.format(namelength, neededlength, longerlength, n.image.name))
                        count_replaced_files += 1
                        old_name = n.image.name
                        new_name = n.image.name
                        new_name = new_name[-neededlength:]
                        n.image.name = new_name
                        info_string = old_name + ' has been replaced with ' + new_name
                        print(info_string)
                    n.image.filepath_raw = "F:/SteamLibrary/steamapps/common/H3EK/tags/bitmaps/" + n.image.name + ".tif"
                    n.image.file_format = "TIFF"
                    n.image.save()

        if s.material is not None:
            old_name = s.material.name
            material = s.material
            nodes = material.node_tree.nodes
            principled = next(n for n in nodes if n.type == 'BSDF_PRINCIPLED')
            base_color = principled.inputs['Base Color']
            link = base_color.links[0]
            link_node = link.from_node
            material.name = os.path.splitext( link_node.image.name )[0] + ".png"
            print( "Material Old Name:", old_name, )
            print( "Material New Name:", material.name )
            count_replaced_files += 1
                
print(str(count_replaced_files))
print('File were renamed')
print(texture_list)

"""
mats = bpy.data.materials
for obj in bpy.data.objects:
    for slt in obj.material_slots:
        part = slt.name.rpartition('.')
        if part[2].isnumeric() and part[0] in mats:
            print(str(obj.name))
            slt.material = mats.get(part[0])
"""
