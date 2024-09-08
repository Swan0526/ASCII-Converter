from PIL import Image, ImageFont, ImageDraw
import numpy as np

# ASCII characters from darkest to lightest
ASCII_CHARS = ["@", "#", "O", "o", "-", ".", " "]

def scale_image(image, new_width=100, font_path="Consolas-Font/Consolas.ttf", font_size=12):
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width)

    # Load the font to calculate the character dimensions
    font = ImageFont.truetype(font_path, font_size)
    char_bbox = font.getbbox('A')  # Use a typical character to calculate the aspect ratio
    char_width = char_bbox[2] - char_bbox[0]
    char_height = char_bbox[3] - char_bbox[1]
    char_aspect_ratio = char_height / char_width

    # Adjust new height by the character aspect ratio
    new_height = int(aspect_ratio * new_width * char_aspect_ratio)
    
    # Resize image while preserving aspect ratio
    resized_image = image.resize((new_width, new_height))
    return resized_image

def convert_grayscale(image):
    return image.convert("L")  # Convert the image to grayscale

def map_pixels_to_ascii(image):
    pixels = np.array(image)
    ascii_str = ""

    num_ascii_chars = len(ASCII_CHARS)-1
    range_width = 256 // num_ascii_chars
    # Map each pixel value to an ASCII character
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // range_width]
    
    return ascii_str

def image_to_ascii(image, new_width=100, font_path="Consolas-Font/Consolas.ttf", font_size=12):
    # Scale the image based on the desired width and convert to grayscale
    image = scale_image(image, new_width, font_path, font_size)
    image = convert_grayscale(image)

    # Map the image pixels to ASCII characters
    pixels = np.array(image)
    ascii_image = "\n".join(
        ["".join(map_pixels_to_ascii(row)) for row in pixels]
    )

    return ascii_image

def create_ascii_image(ascii_image, font_path, font_size, output_file):
    # Split the ASCII image into lines
    lines = ascii_image.split("\n")

    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Calculate image size based on the font size and number of characters
    max_line_length = max(len(line) for line in lines)  # Maximum number of characters in any line
    char_bbox = font.getbbox('a')  # Get the size of a typical character ('A')
    text_width = char_bbox[2] - char_bbox[0]
    text_height = char_bbox[3] - char_bbox[1]

    # Now calculate the actual image size based on the text dimensions
    image_width = max_line_length * text_width  # Width in pixels, based on the number of characters
    image_height = len(lines) * text_height     # Height in pixels, based on the number of lines

    # Create a new image with a white background
    img = Image.new('RGB', (image_width, image_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Draw each line of ASCII text on the image
    y_offset = 0
    for line in lines:
        draw.text((0, y_offset), line, font=font, fill=(0, 0, 0))
        y_offset += text_height

    # Save the image as PNG
    img.save(output_file)
    print(f"ASCII PNG image saved as {output_file}")

def ASCII_Conv(image_path, new_width=100, output_file="ASCII_IMAGE.png", font_path="Consolas-Font/Consolas.ttf", font_size=12):
    # Open the image
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path}. Error: {e}")
        return

    # Convert image to ASCII
    ascii_image = image_to_ascii(image, new_width, font_path, font_size)

    # Create and save the ASCII image as PNG
    create_ascii_image(ascii_image, font_path, font_size, output_file)
    print(f"ASCII art saved as image: {output_file}")
