from PIL import Image
import numpy as np

def image_to_rgb_array(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to RGB
    img_rgb = img.convert('RGB')
    
    # Convert image to a numpy array of RGB values
    rgb_array = np.array(img_rgb)
    
    return rgb_array

def print_rgb_array(rgb_array):
    # Iterate over the 2D array
    rows = []
    for row in rgb_array:
        # Black pixels were changed to transparent values marked by {-1, -1, -1}
        row_str = '{ ' + ', '.join(
            f'{{{-1 if r == 0 and g == 0 and b == 0 else r}, {-1 if r == 0 and g == 0 and b == 0 else g}, {-1 if r == 0 and g == 0 and b == 0 else b}}}'
            for r, g, b in row) + ' }'
        rows.append(row_str)
    print('{', ', '.join(rows), '}')

# Main function
image_path = 'p1.png'
rgb_array = image_to_rgb_array(image_path)

# Print the array
print_rgb_array(rgb_array)