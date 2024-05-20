from PIL import Image, ImageOps, ImageDraw, ImageFont
import base64
from io import BytesIO
import io
import IPython.display as display

# Function to convert an image to a base64 string
def imageToBase64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_str

# Function to convert a base64 string to an image
def base64toImage(base64string):
    img_str = base64.b64decode(base64string)
    image = Image.open(BytesIO(img_str))
    return image

# Function to create a meme with given text
def meme_maker(image, top_text, bottom_text, font_path='impact.ttf'):
    draw = ImageDraw.Draw(image)
    
    # Calculate dynamic font size based on image dimensions
    font_size = min(image.width, image.height) // 10  # scaling factor
    font = ImageFont.truetype(font_path, font_size)

    # Calculate text lengths
    top_text_length = draw.textlength(top_text, font=font)
    bottom_text_length = draw.textlength(bottom_text, font=font)

    # Calculate text positions
    top_text_position = ((image.width - top_text_length) // 2, 10)
    bottom_text_position = ((image.width - bottom_text_length) // 2, image.height - font_size - 10)

    # Outline properties
    outline_color = "white"
    outline_width = 2
    offsets = [-outline_width, outline_width]

    # Draw outline for top text using loops
    for x in offsets:
        for y in offsets:
            draw.text((top_text_position[0] + x, top_text_position[1] + y), top_text, font=font, fill=outline_color)

    # Draw outline for bottom text using loops
    for x in offsets:
        for y in offsets:
            draw.text((bottom_text_position[0] + x, bottom_text_position[1] + y), bottom_text, font=font, fill=outline_color)

    # Draw main text on the image
    draw.text(top_text_position, top_text, font=font, fill="black")
    draw.text(bottom_text_position, bottom_text, font=font, fill="black")

    return image
