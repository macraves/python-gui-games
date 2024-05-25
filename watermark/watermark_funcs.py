"""Adding WaterMark on selected image"""

import os
from PIL import Image, ImageDraw, ImageFont


base_dir = os.path.dirname(__file__)


def remove_white_background(img: Image):
    """docs"""
    new_data = []
    data = img.getdata()
    for item in data:
        if item[0] in list(range(200, 256)):
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    img.putdata(new_data)
    return img


def image_opacity(main_img: Image, img: Image, ratio: int = 50):
    """docs"""
    if img.mode != "RGBA":
        alpha = Image.new("L", img.size, 255)
        img.putalpha(alpha)
    position = (
        main_img.size[0] - img.size[0],
        main_img.size[1] - img.size[1],
    )
    img = remove_white_background(img=img)
    paste_mask = img.split()[3].point(lambda i: i * ratio / 100.0)
    main_img.paste(img, position, mask=paste_mask)
    return main_img


def crop_and_resize(img_path: str, cor=(150, 120, 500, 450)):
    """docs"""
    watermark_img = Image.open(img_path)
    cropped = watermark_img.crop(cor)
    cropped_size = cropped.size
    new_size = (cropped_size[0] // 4, cropped_size[1] // 4)
    resized = cropped.resize(new_size)
    return resized


def text_watermark(photo_path: str, text: str):
    """docs"""
    with Image.open(photo_path).convert("RGBA") as base:
        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
        x, y = base.size
        # get a font
        fnt = ImageFont.load_default()

        # get a drawing context
        d = ImageDraw.Draw(txt)

        # draw text, full opacity
        d.text(((x // 2) - 50, y // 2), text, font=fnt, fill=(255, 255, 255, 255))
        out = Image.alpha_composite(base, txt)
        # Convert image to RGB mode
        out = out.convert("RGB")
        return out


def save_as(image: Image, new_file_name: str):
    """Saves the image.
    Args:
        image (PIL.Image.Image): The image to save.
    """
    new_file_path = os.path.join(base_dir, new_file_name)
    image.save(new_file_path)


def save_image(image: Image, image_file_path: str):
    """docs"""
    image.save(image_file_path)


def paste_watermark(main_path, watermark_path):
    """docs"""
    watermark = crop_and_resize(watermark_path)
    main_photo = Image.open(main_path)
    main_image = image_opacity(main_img=main_photo, img=watermark)
    save_path = os.path.join(base_dir, "watermarked.png")
    main_image.save(save_path)
    text_marked = text_watermark(photo_path=save_path, text="All Rights Reserved")
    text_marked.save(save_path, "PNG")
    return save_path
