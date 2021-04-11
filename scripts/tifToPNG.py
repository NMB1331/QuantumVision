#!/usr/bin/env python
# coding: utf-8

# In[70]:


from PIL import Image
import numpy as np
import os
import sys

"""
Author: Nathan Brown

Converts all .tif files in one folder to png files and saves them in another folder.
Directory containing .tif files is first argument, destination is second.
e.g. python tifToPNG.py C:\Users\YourName\Downloads\data_imgs\tests C:\Users\YourName\Downloads\data_imgs\tests\data
"""

def processTif(tifPath, tifName):
    """Convert a multipage tif to a folder of png files.
    tifPath is path of tif file. tifName is the filename.
    """
    # Convert tif to a numpy array
    data = readTiff(tifPath)
    # Convert frames to png files
    for i in range(len(data)):
        filename = r"C:\Users\Nathan\Downloads\data_imgs\tests\data\{}_{}.png".format(tifName, i)
        # Save frame as png
        toPNG(data[i], filename)
    
def readTiff(path):
    """Convert a multipage tiff to a numpy array
    :param path: path of the tiff file
    """
    img = Image.open(path)
    images = []
    for i in range(img.n_frames):
        img.seek(i)
        images.append(np.array(img))
    return np.array(images)

def toPNG(arr, filepath):
    """Convert one np array to png.
    Outputs to filepath.
    """
    img = Image.fromarray(arr)
    #img.show()
    img.save(filepath)
    
def processFolder(path, dest):
    """Convert all tif files in path dir to png.
    path is directory where tifs are stored
    dest is where pngs should be saved
    """
    for root, dirs, files in os.walk(path):
        for name in files:
            # root is directory, name is filename
            print(os.path.join(root, name))
            if os.path.splitext(os.path.join(root, name))[1].lower() == ".tif":
                # Check for duplicates
                # Needs to be changed to check dest instead of path
                if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".png"):
                    print("A png file already exists for", name)
                else:
                    source = os.path.join(root, name)
                    processTif(source, os.path.splitext(name)[0])
            
if __name__ == "__main__":
    n = len(sys.argv)
    print("{} arguments passed.".format(n))
    
    print("Tif folder:", sys.argv[1])
    print("PNG destination folder:", sys.argv[2])
    
    processFolder(sys.argv[1], sys.argv[2])
    #processFolder(r"C:\Users\Nathan\Downloads\data_imgs\tests", r"C:\Users\Nathan\Downloads\data_imgs\tests\data")

