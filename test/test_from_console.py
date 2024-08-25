
# How to execute this:
# python3 script.py my_custom.py monokai --scenario console



import argparse
from PIL import Image, ImageDraw, ImageFont

def draw_text(draw, text, position, font, max_width, fill):
    """
    Draw wrapped text on an image, ensuring it fits within max_width.
    """
    lines = []
    words = text.split()
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        text_bbox = draw.textbbox((0, 0), test_line, font=font)
        text_width = text_bbox[2] - text_bbox[0]

        if text_width > max_width:
            lines.append(current_line)
            current_line = word
        else:
            current_line = test_line

    lines.append(current_line)  # Add the last line

    y = position[1]
    for line in lines:
        draw.text((position[0], y), line, font=font, fill=fill)
        y += font.getbbox("A")[3] - font.getbbox("A")[1] + 5

    return y  # Return the final y position

def new_image(scenario, text, theme):
    # Define color themes
    themes = {
        'monokai': {'background': (0, 0, 0), 'text': (255, 85, 85), 'line_number': (136, 192, 208)},
        'blackandwhite': {'background': (0, 0, 0), 'text': (255, 255, 255), 'line_number': (200, 200, 200)},
        'solarized': {'background': (0, 43, 54), 'text': (131, 148, 150), 'line_number': (147, 161, 161)},
        'gruvbox': {'background': (40, 28, 22), 'text': (249, 238, 242), 'line_number': (143, 188, 143)},
        'nord': {'background': (46, 52, 64), 'text': (229, 233, 240), 'line_number': (136, 192, 208)}
    }

    # Select the theme colors
    theme_colors = themes.get(theme, themes['blackandwhite'])  # Default to 'blackandwhite' if theme is not found
    background_color = theme_colors['background']
    text_color = theme_colors['text']
    line_number_color = theme_colors['line_number']

    # Load a monospace font
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
    font_size = 20
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()

    # Define padding
    padding = 10

    # Measure the text size to determine image size
    dummy_image = Image.new("RGB", (1, 1))
    dummy_draw = ImageDraw.Draw(dummy_image)
    max_line_width = 0
    total_height = 0

    # Measure line width and total height
    for line in text.strip().split("\n"):
        text_bbox = dummy_draw.textbbox((0, 0), line, font=font)
        line_width = text_bbox[2] - text_bbox[0]
        max_line_width = max(max_line_width, line_width)
        total_height += font.getbbox("A")[3] - font.getbbox("A")[1] + 5

    # Calculate image dimensions
    width = max_line_width + 60  # Adding padding for line numbers and margins
    height = total_height + 20  # Adding padding

    # Create an image with the selected background color
    image = Image.new("RGB", (width, height), background_color)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Draw text lines with line numbers
    y = padding
    for i, line in enumerate(text.strip().split("\n")):
        # Draw line number
        line_number = f"{i + 1:02d} "
        draw.text((padding, y), line_number, font=font, fill=line_number_color)
        
        # Draw text line with wrapping
        y = draw_text(draw, line, (padding + 40, y), font, width - 50, text_color)  # 50 for padding

    # Optionally, add a border to the image
    border_color = (200, 200, 200)  # Border color remains the same
    border_width = 4
    draw.rectangle([border_width, border_width, width-border_width-1, height-border_width-1], outline=border_color)

    # Save the image
    image.save(f"{scenario}_{theme}.png")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate an image from text with different themes.')
    parser.add_argument('file', type=str, help='The path to the file containing the text to draw on the image.')
    parser.add_argument('theme', type=str, choices=['monokai', 'blackandwhite', 'solarized', 'gruvbox', 'nord'], help='The color theme to use for the image.')
    parser.add_argument('--scenario', type=str, choices=['console', 'editor'], default='console', help='The scenario type for the image.')

    args = parser.parse_args()

    # Read text from file
    try:
        with open(args.file, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{args.file}' was not found.")
        return

    # Generate the image
    new_image(args.scenario, text, args.theme)
    print(f"Image for scenario '{args.scenario}' with theme '{args.theme}' saved as '{args.scenario}_{args.theme}.png'.")

if __name__ == "__main__":
    main()

