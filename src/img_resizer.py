from PIL import Image
import os
import glob

def resize_img(target_width_px, target_height_px, img_path):

    if not os.path.exists(img_path + '/resized'):
        os.makedirs(img_path + '/resized')

    target_aspect_ratio = target_width_px / target_height_px

    for filepath in glob.iglob(img_path + "/*.jpg", recursive = True):

        file_name = filepath.split('.')[-2].split("\\")[-1]

        im = Image.open(filepath)
        im_width_px, im_height_px = im.size
        im_aspect_ratio = im_width_px / im_height_px
        left = 0
        right = im_width_px
        bottom = im_height_px
        top = 0

        # Determine dimensions of image to ensure same aspect ratio as original
        if im_aspect_ratio < target_aspect_ratio:  # height of original image needs to be reduced
            while im_aspect_ratio < target_aspect_ratio:
                bottom -= 1
                im_aspect_ratio = right / bottom


        elif im_aspect_ratio > target_aspect_ratio:  # width of original image needs to be reduced
            while im_aspect_ratio > target_aspect_ratio:
                right -= 1
                im_aspect_ratio = right / bottom

        diff_y = im_height_px - bottom
        diff_x = im_width_px - right

        left = diff_x / 2
        right = im_width_px - diff_x / 2
        bottom = im_height_px - diff_y / 2
        top = diff_y / 2

        cropped = im.crop((left, top, right, bottom))

        # Image and target aspect ratios are now identical. Resize.
        new_size = (target_width_px, target_height_px)
        resized = cropped.resize(new_size)

        resized.save(f"{img_path}/resized/{file_name}"+"_resized.jpg")

    print("Done!")