from PIL import Image
import os

# Get current directory
curr_dir = os.getcwd()

def process_image(name):
    """
    To pad images in a directory with 40 pixels on each side (160 pixels in total).
    """
    counter = 1 # Counter for new names
    # Loop through all files in a directory
    for root, dirs, files in os.walk(os.path.join(curr_dir, f'dataset/{name}')):
        for idx, file in enumerate(files): 
            image_path = os.path.join(root, file) # Get file path
            image = Image.open(image_path) # Open image
            
            padded_width = image.width + 160  # 40 pixels on each side
            padded_height = image.height + 160  # 40 pixels on each side
            
            padded_image = Image.new("RGB", (padded_width, padded_height), (238, 238, 238)) # Create a new padded image
            
            x = int((padded_width - image.width) / 2) # Calculate x coordinate
            y = int((padded_height - image.height) / 2) # Calculate y coordinate

            # Paste the original image onto the padded image
            padded_image.paste(image, (x, y))

            # Save the padded image
            output_path = os.path.join(curr_dir, f"processed_dataset/{name}/{name}_{counter}.png") # Get output path
            padded_image.save(output_path) # Save the padded image
            counter += 1 # Increment counter
            
            print(f"Padded image {name} saved:", output_path) # Print output path

if __name__ == "__main__":
    # Create directories
    os.makedirs(os.path.join(curr_dir, "processed_dataset/healthy"), exist_ok=True)
    os.makedirs(os.path.join(curr_dir, "processed_dataset/parkinson"), exist_ok=True)
    # Process images
    process_image("healthy")
    process_image("parkinson")