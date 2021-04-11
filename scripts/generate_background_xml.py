"""
This script will generate XML files for "background" images, i.e. images that don't have any objects defined in them.
These images help the object detector learn to filter out the "background noise", and eliminates some false positives.

Author: Nathaniel M. Burley
Date: 10th April 2021

NOTE/TODO: Seems that you actually aren't supposed to fill in the <object>
"""

import os
import glob


# Function that generates XML files for any .jpgs that don't have them in a directory
# TODO: Get rid of the <object> section
def getBackgroundImages(img_dir):
    os.chdir(img_dir)
    for f in glob.glob("*.jpg"):
        sample_name = str(f).replace(".jpg", "")
        xml_filename = sample_name + ".xml"

        # Check if the XML file exists
        if os.path.isfile(xml_filename):
            pass
        
        # Create the XML if the file doesn't exist, write the necessary text to it
        else:
            full_xml_path = img_dir + "\\" + sample_name + ".xml"
            full_img_path = img_dir + "\\" + sample_name + ".jpg"
            with open(full_xml_path, 'w') as xml_file:
                xml_str = ('<annotation>\n'
                            '<folder>images</folder>\n'
                            '<filename>{}</filename>\n'
                            '<path>{}</path>\n'
                            '<source>\n'
                            '    <database>Unknown</database>\n'
                            '</source>\n'
                            '<size>\n'
                            '    <width>256</width>\n'
                            '    <height>256</height>\n'
                            '    <depth>1</depth>\n'
                            '</size>\n'
                            '<segmented>0</segmented>\n'
                        '</annotation>').format(f, full_img_path)

                # Write the string to the file
                xml_file.write(xml_str)
                xml_file.close()
                print("Created file {}".format(full_xml_path))



if __name__ == "__main__":
    img_dir = "C:\\Users\\NMB1331\\QuantumVision\\TensorFlow\\workspace\\training_demo\\images\\train"
    getBackgroundImages(img_dir)
