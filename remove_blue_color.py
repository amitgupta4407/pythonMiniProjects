import cv2
import numpy as np
import matplotlib.pyplot as plt

def remove_blue_background(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([60, 100, 0])
    upper_blue = np.array([160, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Apply morphological opening to remove noise
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=12)

    # Set alpha channel (transparency) to 0 for blue regions
    alpha_channel = np.ones(mask.shape, dtype=np.uint8) * 255
    alpha_channel[mask != 0] = 0

    # Merge alpha channel with the original image
    res = cv2.merge((image, alpha_channel))
    return res

# calling remove_blue_background for rice.jpg image
img = cv2.imread(r"C:\Users\cvcla\OneDrive\Desktop\BlueBack\NumberParboiled\IMG_20230717_0001.jpg")
res = remove_blue_background(img)

# Save the processed image as PNG (supports transparency)
output_path = r"IMG_20230717_0001_processed.png"
cv2.imwrite(output_path, res)

# Convert BGR to RGB for matplotlib display
res_rgb = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)

# Display the processed image using matplotlib
plt.imshow(res)
plt.axis("off")
plt.show()
