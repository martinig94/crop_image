import os
import PIL as pl
from PIL import Image
from typing import Optional


def crop_image(
    image,
    reference: Optional = None,
    width_ref: Optional = None,
    height_ref: Optional = None,
    save: bool = True,
):
    """
    Crop images following a reference image or following the width_ref and height_ref.
    If a reference image and a width and height reference are provided the reference image is used.

    Args:
        image: filepath to image to be cropped
        reference: reference image
        width_ref: reference width
        height_ref: reference height
        save: boolean value to save cropped image in dedicated `cropped` directory in the working directory

    Returns:
        cropped_image: cropped image

    """

    with Image.open(image) as img:
        if reference is not None:
            with pl.Image.open(reference) as img_ref:
                width_ref, height_ref = img_ref.size
        elif width_ref is not None and height_ref is None:
            raise ValueError(
                'If "width_ref"is provided, also "height_ref"must be provided'
            )
        elif width_ref is None and height_ref is not None:
            raise ValueError(
                'If "height_ref"is provided, also "width_ref"must be provided'
            )
        elif width_ref is None and height_ref is None and reference is None:
            raise ValueError(
                'wither a "reference" or "width_ref" and "height_ref" must be provided'
            )
        width, height = img.size
        x_coord_left = (width - width_ref) / 2
        x_coord_right = (width - width_ref) / 2 + width_ref
        y_coord_up = (height - height_ref) / 2
        y_coord_bottom = (height - height_ref) / 2 + height_ref
        cropped_image = img.crop(
            (x_coord_left, y_coord_up, x_coord_right, y_coord_bottom)
        )
        if save:
            CROPPED_DIR = os.path.join(os.getcwd(), "cropped")
            if not os.path.exists(CROPPED_DIR):
                os.makedirs(CROPPED_DIR)
            cropped_image.save(os.path.join(CROPPED_DIR, image))
        return cropped_image


