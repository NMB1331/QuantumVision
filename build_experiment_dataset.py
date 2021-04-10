"""
Contains functions for importing, formatting, and otherwise manipulating the dataset.

NOTE: https://machinelearningmastery.com/how-to-load-and-manipulate-images-for-deep-learning-in-python-with-pil-pillow/
Super helpful overview: https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491

Author: Nathaniel M. Burley
Date Created: 21st January 2021
Last Modified By: Nathaniel M. Burley
Date Last Modified: 22nd January 2021
"""
from PIL import Image
import pandas as pd
import numpy as np
import json

IMAGE_HEIGHT = 249  # Temp value. Assumes 249x425 image
IMAGE_WIDTH = 425



# Function that parses the region_shape_attribute JSON to get the coordinates of the bottom left, top right corner
# The neural network will ultimately predict [x, y, width, height]
# TODO: Instead need width, height, and center of box
def getLabelsFromJSONStr(region_shape_attribute_list):
    label_list = []
    for label_json in region_shape_attribute_list:
        label_json = json.loads(label_json)
        #print("Lower left X-coordinate, Y-coordinate: ({},{})".format(label_json['x'], label_json['y']))
        box_label = [label_json['x'], label_json['y'], label_json['width'], label_json['height']]
        label_list.append(box_label)
    return label_list


# Function that creates key values pairs of image and labels
def loadPathsAndLabels(image_path_csv="test_annotation_file.csv"):
    image_labels_dict = {}
    data_df = pd.read_csv(image_path_csv)

    # Get image and list of JSON labels
    for image_name in data_df['filename']:
        full_image_name = "data/" + image_name
        if full_image_name not in image_labels_dict.keys():
            label_values = list(data_df.loc[data_df['filename'] == image_name, 'region_shape_attributes'])
            image_labels_dict[full_image_name] = getLabelsFromJSONStr(label_values)
            print(image_labels_dict[full_image_name])  # For debugging
    
    # Return image name and list of labels/coordinates
    return image_labels_dict


# Function that loads images and labels into numpy arrays
# TODO: Build the list of labels (Y_data array)
def buildDataset(image_path_csv="test_annotation_file.csv"):
    # Load in the images and data
    images_and_labels = loadPathsAndLabels(image_path_csv)
    NUM_IMAGES = len(images_and_labels.keys())
    X_data = np.zeros((IMAGE_HEIGHT, IMAGE_WIDTH, 4))

    # Read in all the images, and add to X_data array
    for image_name, counter in zip(images_and_labels.keys(), range(0,NUM_IMAGES)):
        # Read in a new image
        image = Image.open(image_name)
        image_arr = np.asarray(image)

        # Add the new image to the X data array
        if counter == 0:
            X_data = image_arr
        else:
            X_data = np.stack((X_data, image_arr))
    
    # Display the shape, return the X data
    print("Dataset shape: {}".format(X_data.shape))
    return X_data, None


# TODO: Comment this out, move main to another file
if __name__ == "__main__":
    X_data, Y_data = buildDataset()