import torch
from torchvision.transforms import v2
from PIL import Image
import matplotlib.pyplot as plt

# Loading images
image_1 = Image.open("Mini-project_Instagram/image_1.jpeg")
image_2 = Image.open("Mini-project_Instagram/image_2.jpeg")
image_3 = Image.open("Mini-project_Instagram/image_3.jpeg")

# Random changes in brightness, contrast and saturation
jitter = v2.ColorJitter(brightness=[0.8,1.2], contrast =[0.8,1.2], saturation=[0.8,1.2])
jittered_image_1 = [jitter(image_1) for _ in range(5)]
jittered_image_2 = [jitter(image_2) for _ in range(5)]
jittered_image_3 = [jitter(image_3) for _ in range(5)]

# Random sharpness adjustment
sharpness = v2.RandomAdjustSharpness(sharpness_factor=2, p=0.5)
sharpened_image_1 = [sharpness(image_1) for _ in range(5)]
sharpened_image_2 = [sharpness(image_2) for _ in range(5)]
sharpened_image_3 = [sharpness(image_3) for _ in range(5)]

# Creating lists of images
jittered_images_list = [jittered_image_1, jittered_image_2, jittered_image_3]
sharpened_images_list = [sharpened_image_1, sharpened_image_2, sharpened_image_3]

# Showing synthetic data of the 1,2,3 image
for x in range(3):
    fig, axs = plt.subplots(2, 5)

    for i in range(5):
        axs[0,i].imshow(jittered_images_list[x][i])
        axs[0,i].axis("off")

        axs[1,i].imshow(sharpened_images_list[x][i])
        axs[1,i].axis("off")

    fig.text(0.25, 0.88, "Synthetic Data: Brightness, Contrast, Saturation")
    fig.text(0.35, 0.46, "Synthetic Data: Sharpness")

    fig.suptitle(f"Synthetic Data Augmentation {x+1}")
    plt.show()