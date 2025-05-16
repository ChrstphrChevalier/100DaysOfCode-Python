from PIL import Image, ImageDraw, ImageFont

def add_text_watermark(image_path, text, position="bottom_right", color="#FFFFFF", size=20):
    image = Image.open(image_path).convert("RGBA")
    watermark_layer = Image.new("RGBA", image.size, (0, 0, 0, 0))

    draw = ImageDraw.Draw(watermark_layer)
    try:
        font = ImageFont.truetype("arial.ttf", size)
    except:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    margin = 10
    width, height = image.size

    if position == "bottom_right":
        x = width - text_width - margin
        y = height - text_height - margin
    elif position == "bottom_left":
        x = margin
        y = height - text_height - margin
    elif position == "top_left":
        x = margin
        y = margin
    elif position == "top_right":
        x = width - text_width - margin
        y = margin
    elif position == "center":
        x = (width - text_width) // 2
        y = (height - text_height) // 2

    draw.text((x, y), text, font=font, fill=color)
    combined = Image.alpha_composite(image, watermark_layer)
    return combined.convert("RGB")