# Development 

### What is happening here?

1. `preprocess.py` is used to preprocess the data. It pads each images with 40pixel, and them will be resized to 160 x 160. This is done to make the data more uniform and easier to train. 
2. `rename.py` is used to renames the images. It renames the images to the format of `label_number.jpg`. This is done to make it easier to load the data.