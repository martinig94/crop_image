import pytest
from crop_image.main import crop_image


def test_crop_image_no_inputs():
    with pytest.raises(ValueError):
        crop_image()


def test_crop_image_no_height():
    with pytest.raises(ValueError):
        crop_image(width_ref=5)


def test_crop_image_no_width():
    with pytest.raises(ValueError):
        crop_image(height_ref=5)
