import os
import glob

"""

These are 40 character long textures used in the character slots in the default_3 shader used to generate templates
________________________________________

5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F

materials renamed to texture names, 40 char long
40 char long tifs exported to tags/bitmaps
gimp fixes tifs to data/objects/bitmaps/custom
generate blader shaders to testone/shaders 40 chars long
generate bitmaps to  tags/objects/bitmaps/custom
run this script
"""
uppersource_str = '5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F5F'    #The name of the bitmap in the shader. 80 characters long.
source_str=uppersource_str.lower()
charlimit = 40
default_directory='F://SteamLibrary//steamapps//common//H3EK//tags//levels//multi//testone//shaders//' #The directory with your blader generated shaders
for i in glob.glob(default_directory + '*.shader', recursive=True): #Goes through all the shader files in this directory
    filename=os.path.basename(i).lower() #Gets the file name
    basename=os.path.splitext(filename)[0] #Strips the .shader
    replace_str=basename.encode('utf-8') #encodes the stripped file name in utf-8
    replace_str=replace_str.hex() #converts the file name into hex

    with open(i, 'rb') as f:
        content = f.read().hex() #Reads the shader

    print(source_str in content)
    print(len(replace_str))
    if source_str in content and len(replace_str) == 2*charlimit:

        #Replaces the bitmap with the name of the shader in hex
        print('Passes')
        content = content.replace(source_str, replace_str)

        with open(i, 'wb') as f:
            f.write(bytes.fromhex(content)) #Writes the changes to the shader.

    if source_str not in content and len(replace_str) == 2*charlimit:
        print('Could not find ' + source_str + ' in ' + filename)

    if source_str in content and len(replace_str) != 2*charlimit:
        print('Your ' + replace_str + ' needs to be ' + str(charlimit) + ' characters long')

    if source_str not in content and len(replace_str) != 2*charlimit:
        print('Could not find ' + source_str + ' and your ' + replace_str + ' needs to be ' + str(charlimit) + ' characters long')

    f.close()
    with open(i, 'rb') as f:
        new_content = f.read().hex() #Double checks the new file to be sure it was replaced
print(source_str + " in `shader`:", source_str in new_content) #Prints output
