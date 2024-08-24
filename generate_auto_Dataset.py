import os
import numpy as np
from shutil import copy2
from PIL import Image

# Function to calculate NDVI and classify the image
def process_image(image_path):
    image = np.array(Image.open(image_path))

    # Extract the red, green, and NIR channels
    red_channel = np.copy(image[:, :, 0])
    green_channel = np.copy(image[:, :, 1])
    nir_channel = np.copy(image[:, :, 2])

    red_channel = red_channel.astype(np.float32)
    green_channel = green_channel.astype(np.float32)
    nir_channel = nir_channel.astype(np.float32)

    red_channel[red_channel<170] = 0
    green_channel[green_channel<170] = 0
    nir_channel[nir_channel<170] = 0

    # Calculate NDVI with error handling for division by zero
    ndvi = (nir_channel - red_channel) / (nir_channel + red_channel)
    ndvi[np.isnan(ndvi)] = 0

    n_ndvi = np.count_nonzero(ndvi)
    x_ndvi = np.sum(ndvi)
    avg_ndvi = x_ndvi / n_ndvi if n_ndvi != 0 else 0

    if avg_ndvi <= 0:
        label = "Dead Plants"
    elif avg_ndvi <= 0.30:
        label = "Unhealthy Plants"
    elif avg_ndvi <= 0.60:
        label = "Moderately Healthy Plants"
    else:
        label = "Very Healthy Plants"

    return label

# Main function to process all images in a directory
def main():
    input_dir = 'E:\\Dataset Multispectral\\Dataset_Mapir\\CroppedRGN_Unpad\\2024_0622'
    output_dir = 'E:\\Dataset Multispectral\\Dataset_Mapir\\SegmentLabelRGN_Unpad'
    copy_dir = 'E:\\Dataset Multispectral\\Dataset_Mapir\\NormalRGN_Unpad\\2024_0613'
    # date = '2024_0615'
    
    # Create output directories if they don't exist
    labels = ["Dead Plants", "Unhealthy Plants", "Moderately Healthy Plants", "Very Healthy Plants"]
    for label in labels:
        os.makedirs(os.path.join(output_dir, label), exist_ok=True)

    # Process each image in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".png") or filename.endswith(".JPG") or filename.endswith(".tif"):
            image_path = os.path.join(input_dir, filename)
            label = process_image(image_path)
            # dest_path = os.path.join(output_dir, label, filename)
            # copy2(image_path, dest_path)
            
            # Copy the image from the copy_dir to the same label folder
            original_image_path = os.path.join(input_dir, filename)
            folder_name = os.path.basename(input_dir)
            new_filename = f"{folder_name}_{filename}"
            if os.path.exists(original_image_path):
                copy2(original_image_path, os.path.join(output_dir, label, new_filename))
            
            print(f"Processed {filename}: {label}")

if __name__ == "__main__":
    main()
