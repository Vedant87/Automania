import numpy as np
import cv2

def color_thresh(img, rgb_thresh=(____, ____, ____)):
    color_select = np.zeros_like(img[:, :, 0])
    above_thresh = (img[:, :, 0] > rgb_thresh[0]) \
                & (img[:, :, 1] > rgb_thresh[1]) \
                & (img[:, :, 2] > rgb_thresh[2])
    color_select[above_thresh] = 1
    return color_select

def rover_coords(binary_img):
    ypos, xpos = binary_img.nonzero()
    x_pixel = ____(ypos - binary_img.shape[0]).astype(np.float)
    y_pixel = ____(xpos - binary_img.shape[1] / 2).astype(np.float)
    return x_pixel, y_pixel

def to_polar_coords(x_pixel, y_pixel):
    dist = np.sqrt(____**2 + y_pixel**2)
    angles = np.arctan2(____, x_pixel)
    return dist, angles

def rotate_pix(xpix, ypix, yaw):
    yaw_rad = ____ * np.pi / 180
    xpix_rotated = (xpix * np.cos(yaw_rad)) - (ypix * np.sin(yaw_rad))
    ypix_rotated = (xpix * np.sin(yaw_rad)) + (ypix * np.cos(yaw_rad))
    return xpix_rotated, ypix_rotated

def translate_pix(xpix_rot, ypix_rot, xpos, ypos, scale):
    xpix_translated = (xpix_rot / ____) + xpos
    ypix_translated = (ypix_rot / ____) + ypos
    return xpix_translated, ypix_translated

def pix_to_world(____, ____, xpos, ypos, yaw, world_size, scale):
    xpix_rot, ypix_rot = rotate_pix(____, ____, yaw)
    xpix_tran, ypix_tran = translate_pix(____, ____, xpos, ypos, scale)
    x_pix_world = np.clip(np.int_(xpix_tran), 0, world_size - 1)
    y_pix_world = np.clip(np.int_(ypix_tran), 0, world_size - 1)
    return x_pix_world, y_pix_world

def perspect_transform(____, src, dst):
    M = cv2.getPerspectiveTransform(____, ____)
    warped = cv2.warpPerspective(____, M, (img.shape[1], img.shape[0]))
    return warped


# Apply the above functions in succession and update the Rover state accordingly
def perception_step(Rover):
    # Perform perception steps to update Rover()
    # TODO: 
    # NOTE: camera image is coming to you in Rover.img
    # 1) Define source and destination points for perspective transform
    # 2) Apply perspective transform
    # 3) Apply color threshold to identify navigable terrain/obstacles/rock samples
    # 4) Update Rover.vision_image (this will be displayed on left side of screen)
        # Example: Rover.vision_image[:,:,0] = obstacle color-thresholded binary image
        #          Rover.vision_image[:,:,1] = rock_sample color-thresholded binary image
        #          Rover.vision_image[:,:,2] = navigable terrain color-thresholded binary image

    # 5) Convert map image pixel values to rover-centric coords
    # 6) Convert rover-centric pixel values to world coordinates
    # 7) Update Rover worldmap (to be displayed on right side of screen)
        # Example: Rover.worldmap[obstacle_y_world, obstacle_x_world, 0] += 1
        #          Rover.worldmap[rock_y_world, rock_x_world, 1] += 1
        #          Rover.worldmap[navigable_y_world, navigable_x_world, 2] += 1

    # 8) Convert rover-centric pixel positions to polar coordinates
    # Update Rover pixel distances and angles
        # Rover.nav_dists = rover_centric_pixel_distances
        # Rover.nav_angles = rover_centric_angles
    
 
    
    
    return Rover