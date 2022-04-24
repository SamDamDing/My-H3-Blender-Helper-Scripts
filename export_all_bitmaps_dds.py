import glob
import subprocess
"""
██╗    ██╗ █████╗ ██████╗ ███╗   ██╗██╗███╗   ██╗ ██████╗ 
██║    ██║██╔══██╗██╔══██╗████╗  ██║██║████╗  ██║██╔════╝ 
██║ █╗ ██║███████║██████╔╝██╔██╗ ██║██║██╔██╗ ██║██║  ███╗
██║███╗██║██╔══██║██╔══██╗██║╚██╗██║██║██║╚██╗██║██║   ██║
╚███╔███╔╝██║  ██║██║  ██║██║ ╚████║██║██║ ╚████║╚██████╔╝
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                          

███████╗███████╗████████╗    ██╗   ██╗ ██████╗ ██╗   ██╗██████╗     ██████╗ ██╗██████╗ ███████╗ ██████╗████████╗ ██████╗ ██████╗ ██╗███████╗███████╗
██╔════╝██╔════╝╚══██╔══╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗    ██╔══██╗██║██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██║██╔════╝██╔════╝
███████╗█████╗     ██║        ╚████╔╝ ██║   ██║██║   ██║██████╔╝    ██║  ██║██║██████╔╝█████╗  ██║        ██║   ██║   ██║██████╔╝██║█████╗  ███████╗
╚════██║██╔══╝     ██║         ╚██╔╝  ██║   ██║██║   ██║██╔══██╗    ██║  ██║██║██╔══██╗██╔══╝  ██║        ██║   ██║   ██║██╔══██╗██║██╔══╝  ╚════██║
███████║███████╗   ██║          ██║   ╚██████╔╝╚██████╔╝██║  ██║    ██████╔╝██║██║  ██║███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║██║███████╗███████║
╚══════╝╚══════╝   ╚═╝          ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝
                                                                                                                                                    
"""

tagsdirectory = r'F:/SteamLibrary/steamapps/common/H3EK/tags/'
tagsdirectory = tagsdirectory.replace("/", '\\' )
h3ek = r'F:\SteamLibrary\steamapps\common\H3EK'
toolpath = r'F:\SteamLibrary\steamapps\common\H3EK\tool.exe'
exportdirectory = r'F:\SteamLibrary\steamapps\common\H3EK\tags\bitmaps_dump/' #Create this if you don't have it

def extract_bitmaps(toolpath, directory, exportdirectory):
    for i in glob.glob(tagsdirectory + '**/*.bitmap', recursive=True):
        BitmapPath = i
        BitmapPath = str(BitmapPath.split(h3ek)[1])
        BitmapPath = str(BitmapPath.split("tags\\")[1])
        BitmapPath = str(BitmapPath.split(".bitmap")[0])
        print("Exporting bitmaps in " + directory)
        result = subprocess.Popen([toolpath, "export-bitmap-dds", BitmapPath, exportdirectory], cwd=h3ek)

extract_bitmaps(toolpath, tagsdirectory, exportdirectory)
