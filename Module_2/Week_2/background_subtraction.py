import numpy as np
import cv2
import os

# Read images and resize
bg1_image = cv2.imread(
    'AIO2024_Exercise/Module_2/Week_2/GreenBackground.png', 1)
bg1_image = cv2.resize(bg1_image, (678, 381))

ob_image = cv2.imread('AIO2024_Exercise/Module_2/Week_2/Object.png', 1)
ob_image = cv2.resize(ob_image, (678, 381))

bg2_image = cv2.imread('AIO2024_Exercise/Module_2/Week_2/NewBackground.jpg', 1)
bg2_image = cv2.resize(bg2_image, (678, 381))

# Compute Difference


def compute_difference(bg_img, input_img):
    difference_three_channel = cv2.absdiff(bg_img, input_img)
    difference_single_channel = np.sum(difference_three_channel, axis = 2) / 3.0
    difference_single_channel = difference_single_channel.astype('uint8')

    return difference_single_channel

# Compute Binary Mask


def compute_binary_mask(difference_single_channel):
    difference_binary = np.where(difference_single_channel >= 15, 255, 0).astype('uint8')
    difference_binary = np.stack((difference_binary,) * 3, axis = -1)
    return difference_binary

# Replace Background
def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(bg1_image, ob_image)
    binary_mask = compute_binary_mask(difference_single_channel)
    output = np.where(binary_mask == 255, ob_image, bg2_image)
    return output


difference_single_channel = compute_difference(bg1_image, ob_image)
binary_mask = compute_binary_mask(difference_single_channel)
new_background = replace_background(bg1_image, bg2_image, ob_image)

cv2.imshow('Difference', difference_single_channel)
cv2.imshow('Binary Mask', binary_mask)
cv2.imshow('New Background', new_background)
cv2.waitKey(0)
cv2.destroyAllWindows()
