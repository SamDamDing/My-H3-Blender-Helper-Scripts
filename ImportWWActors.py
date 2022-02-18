# Import json Python module
import json
import bpy
#from ActorDict import ActorDict #I took a bunch of the actordatabase jsons from Winditor and merged them to form some sort of dictionary. It's huuuuge and has all the actor information in it. Probably won't release it.
file = open("sea.json", 'r') #This is a json you can get you ctrl+a and ctrl+c the actors on the sea stage using Winditor.
json_data = json.load(file)

def actorimporttranslate():
        bpy.ops.wm.collada_import(
        filepath = ObjPath,
        auto_connect = True,
        find_chains = True,
        fix_orientation = True)
        
        bpy.ops.transform.translate(
        value=(posX, -posZ, posY), 
        orient_axis_ortho='X', 
        orient_type='GLOBAL', 
        orient_matrix=(
        (1, 0, 0), 
        (0, 1, 0), 
        (0, 0, 1)), 
        orient_matrix_type='GLOBAL', 
        constraint_axis=(True, False, False), 
        mirror=False, 
        use_proportional_edit=False, 
        proportional_edit_falloff='SMOOTH', 
        proportional_size=1, 
        use_proportional_connected=False, 
        use_proportional_projected=False, 
        release_confirm=True)
        """
        bpy.ops.transform.rotate(
        value=rotX, 
        orient_axis='X', 
        orient_type='GLOBAL', 
        orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), 
        orient_matrix_type='GLOBAL', 
        constraint_axis=(True, False, False), 
        mirror=False, 
        use_proportional_edit=False, 
        proportional_edit_falloff='SMOOTH', 
        proportional_size=1, 
        use_proportional_connected=False, 
        use_proportional_projected=False, 
        release_confirm=True)
        
        bpy.ops.transform.rotate(
        value=rotY, 
        orient_axis='Y', 
        orient_type='GLOBAL', 
        orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), 
        orient_matrix_type='GLOBAL', 
        constraint_axis=(True, False, False), 
        mirror=False, 
        use_proportional_edit=False, 
        proportional_edit_falloff='SMOOTH', 
        proportional_size=1, 
        use_proportional_connected=False, 
        use_proportional_projected=False, 
        release_confirm=True)
        
        bpy.ops.transform.rotate(
        value=rotZ, 
        orient_axis='Z', 
        orient_type='GLOBAL', 
        orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), 
        orient_matrix_type='GLOBAL', 
        constraint_axis=(True, False, False), 
        mirror=False, 
        use_proportional_edit=False, 
        proportional_edit_falloff='SMOOTH', 
        proportional_size=1, 
        use_proportional_connected=False, 
        use_proportional_projected=False, 
        release_confirm=True)
        
        bpy.ops.transform.resize(
        value=(scaleX, scaleY, scaleZ), 
        orient_type='GLOBAL', 
        orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), 
        orient_matrix_type='GLOBAL', 
        mirror=False, 
        use_proportional_edit=False, 
        proportional_edit_falloff='SMOOTH', 
        proportional_size=1, 
        use_proportional_connected=False, 
        use_proportional_projected=False, 
        release_confirm=True)
        
        bpy.ops.transform.resize(value=(0.45, 0.45, 0.45), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, True, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
        bpy.ops.object.select_all(action='DESELECT')
        """
#This is just the Oyashi Palm Tree for now, but I could theoretically use it to import any other actor from WW into blender.
ImportedActorName = 'Oyashi'

print(type(json_data))
for each in json_data:
    if 'Name' not in each:
        each['Name']=''
    if ImportedActorName in each['Name']:
        print(each['Name'])
        ObjName=each['Name']
        #Prints Position
        print(each['Transform'].get('Position').get('X'))
        print(each['Transform'].get('Position').get('Y'))
        print(each['Transform'].get('Position').get('Z'))
        #Sets the Position variable for import
        posX=each['Transform'].get('Position').get('X')
        posY=each['Transform'].get('Position').get('Y')
        posZ=each['Transform'].get('Position').get('Z')
        #Prints Rotation
        print(each['Transform'].get('Rotation').get('X'))
        print(each['Transform'].get('Rotation').get('Y'))
        print(each['Transform'].get('Rotation').get('Z'))
        #Sets the Rotation variable for import
        rotX=each['Transform'].get('Rotation').get('X')
        rotY=each['Transform'].get('Rotation').get('Y')
        rotZ=each['Transform'].get('Rotation').get('Z')
        #Prints Local Scale
        print(each['Transform'].get('LocalScale').get('X'))
        print(each['Transform'].get('LocalScale').get('Y'))
        print(each['Transform'].get('LocalScale').get('Z'))
        #Sets the Scale variable for import
        scaleX=each['Transform'].get('LocalScale').get('X')
        scaleY=each['Transform'].get('LocalScale').get('Y')
        scaleZ=each['Transform'].get('LocalScale').get('Z')
        #Gets the Path of the object model
        """
        for i in ActCombDict:
            if ObjName in i:
                ObjPath=ActCombDict[i].get('Models')[0].get('Path')
                print(ObjPath)
        """
        ObjPath = "I:\\Wind Waker HD Extracted\\Oyashi\\Oyashi\\oyashi.dae" #This is the directory to my extracted model. It's normally in the comment block above. This is just an example.
        actorimporttranslate()

file.close()

