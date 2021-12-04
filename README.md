# Introduction
Links for dataset of radish in wheat, can be used for weed detection algorithm training.  Supporting data management python scripts provided, including methods to reformat image labels from PascalVOC to YOLO, view labels YOLO labels, and generate datasets with training, test and validation splits.

This work is part of my undergraduate thesis project on optimising deep learning weed detection by camera angle.  The radish-in-wheat data presented here was used to train a YOLOv5s model.  A 30-degree angle looking forward was found to give best results by comparing precision, recall and mean average precision with 0, 45 and 60 degree camera angles.

An MIT open source license is also provided.


# Source dataset and models
The dataset is available at the following public Google Drive link: https://drive.google.com/drive/u/0/folders/1YzBs7xyn4xnmcCpvmafjHVy9nWXbDN_Z

The trained YOLOv5smodel weights are also available in this folder.

# Data management scripts
These python scripts were written by myself to assist with handling the data.  They can be customised, and may be of some use.
