"""
File that takes in the CSV labels and generates a csv file with the information for a TF Record.

Author: Nathaniel M. Burley
Date Last Modified: 11th April 2021
"""

import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        value = None
        object_exists = root.find("object")
        if object_exists is not None:
            for member in root.findall('object'):
                value = (root.find('path').text,
                                int(root.find('size')[0].text),
                                int(root.find('size')[1].text),
                                member[0].text,
                                int(member[4][0].text),
                                int(member[4][1].text),
                                int(member[4][2].text),
                                int(member[4][3].text)
                        )
                xml_list.append(value)
        else:
            value = (root.find('path').text,
                        int(root.find('size')[0].text),
                        int(root.find('size')[1].text),
                        '-1',
                        '-1',
                        '-1',
                        '-1',
                        '-1'
                    )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df



if __name__ == "__main__":
    #image_path = os.path.join(os.getcwd(), 'annotations')
    image_path = "C:\\Users\\NMB1331\\QuantumVision\\TensorFlow\\workspace\\training_demo\\images\\train"
    xml_df = xml_to_csv(image_path)
    xml_df.to_csv('dot_train_labels.csv', index=None)
    print('Successfully converted xml to csv.')