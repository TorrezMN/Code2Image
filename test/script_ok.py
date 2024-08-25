#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created on: 2024-08-25
# Author: Torrez, Milton 




from PIL import Image, ImageDraw, ImageFont

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

    # Create an image with the selected background color
    width, height = 800, 400
    image = Image.new("RGB", (width, height), background_color)

    # Load a monospace font
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
    font_size = 20
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Define text position and line height
    text_position = (10, 10)
    line_height = font.getbbox("A")[3] - font.getbbox("A")[1] + 5

    # Split text into lines
    lines = text.strip().split("\n")
    for i, line in enumerate(lines):
        # Draw line number
        line_number = f"{i + 1:02d} "
        draw.text((text_position[0], text_position[1] + i * line_height), line_number, font=font, fill=line_number_color)
        
        # Draw text line
        draw.text((text_position[0] + 40, text_position[1] + i * line_height), line, font=font, fill=text_color)

    # Optionally, add a border to the image
    border_color = (200, 200, 200)  # Border color remains the same
    border_width = 4
    draw.rectangle([border_width, border_width, width-border_width-1, height-border_width-1], outline=border_color)

    # Save the image
    image.save(f"{scenario}_{theme}.png")

# Test each color scheme for console and editor scenarios
def run_tests():
    color_schemes = ['monokai', 'blackandwhite', 'solarized', 'gruvbox', 'nord']
    console_text = """
user@linux:~$ ls
Desktop  Documents  Downloads  Music  Pictures  Videos
user@linux:~$ echo 'Hello, World!'
Hello, World!
user@linux:~$
"""
    editor_text = """
function greet(name) {
    console.log('Hello, ' + name + '!');
}

greet('World');
"""

    for theme in color_schemes:
        # Test for console scenario
        new_image('console', console_text, theme)
        print(f"Console test with theme '{theme}' saved.")

        # Test for editor scenario
        new_image('editor', editor_text, theme)
        print(f"Editor test with theme '{theme}' saved.")

if __name__ == "__main__":
    run_tests()

