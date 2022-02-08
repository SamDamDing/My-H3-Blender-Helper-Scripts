import bpy

# the main looping code snippet is modified from
# https://blender.stackexchange.com/questions/80773/how-to-get-the-name-of-image-of-image-texture-with-python

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
                        
print(str(count_replaced_files))
print('File were renamed')
print(texture_list)
