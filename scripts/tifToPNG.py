#!/usr/bin/env python
# coding: utf-8

# In[81]:


from PIL import Image
import numpy as np
import os
import sys
import tkinter.filedialog
import tkinter as tk

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
                    
class App(object):
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()
        self.text = tk.Text()
        self.text.pack()
 
        menu = tk.Menu(master)
        root.config(menu=menu)
        # file menu
        filemenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Set input folder", command=self.setInputFolder)
        filemenu.add_command(label="Set output folder", command=self.setOutputFolder)   
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.do_exit)
        
        self.inputFolder = ""
        self.outputFolder = ""
        
        self.setText("Input folder: " + self.inputFolder + "\nOutput folder: " + self.outputFolder)
        
    def setInputFolder():
        filename = tk.filedialog.askopenfilename(title="Choose a Zoom chat file to open.", filetypes = [("Text Files", "*.txt"), ("All files", "*.*")])
        temp = tk.filedialog.askdirectory(title="Choose source for tif files")
        self.inputFolder = temp
        self.setText("Input folder: " + self.inputFolder + "\nOutput folder: " + self.outputFolder)
        
    def setOutputFolder():
        self.outputFolder = tk.filedialog.askdirectory(title="Choose destination for png files")
        self.setText("Input folder: " + self.inputFolder + "\nOutput folder: " + self.outputFolder)

    def setText(self, txt):
        """Writes text to the editor window."""
        if txt != None:
            self.text.delete(0.0, tk.END)
            self.text.insert(tk.END, txt) 

    def do_exit(self):
        root.destroy()
            
if __name__ == "__main__":
    n = len(sys.argv)
    if n >= 3:
        print("{} arguments passed.".format(n))
        print("Tif folder:", sys.argv[1])
        print("PNG destination folder:", sys.argv[2])
        
        #processFolder(r"C:\Users\YourName\Downloads\data_imgs\tests", r"C:\Users\YourName\Downloads\data_imgs\tests\data")
        #processFolder(sys.argv[1], sys.argv[2])
    
        root = tk.Tk()
        root.title("TIF to PNG Converter")
        app = App(root)
        root.mainloop()
        
    

