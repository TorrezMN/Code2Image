#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created on: 2024-08-25
# Author: Torrez, Milton 

# How to execute this:
# python3 -m code2image.code2image.fotetizar test_file.js monokai --scenario console

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
        text_width, text_height = draw.textsize(test_line, font=font)
        
        if text_width > max_width:
            lines.append(current_line)
            current_line = word
        else:
            current_line = test_line
    
    lines.append(current_line)  # Add the last line

    y = position[1]
    for line in lines:
        draw.text((position[0], y), line, font=font, fill=fill)
        y += text_height + 5  # Add spacing between lines

    return y  # Return the final y position

def new_image(scenario, text, theme):
    # Define color themes
    themes = {
        'blackandwhite': {'background': (0, 0, 0), 'text': (255, 255, 255), 'line_number': (200, 200, 200)},
        'solarized': {'background': (0, 43, 54), 'text': (131, 148, 150), 'line_number': (147, 161, 161)},
        'gruvbox': {'background': (40, 28, 22), 'text': (249, 238, 242), 'line_number': (143, 188, 143)},
        'nord': {'background': (46, 52, 64), 'text': (229, 233, 240), 'line_number': (136, 192, 208)},
        'dracula': {'background': (40, 42, 54), 'text': (248, 248, 242), 'line_number': (98, 114, 164)},
        'github': {'background': (255, 255, 255), 'text': (0, 0, 0), 'line_number': (200, 200, 200)},
        'one_dark': {'background': (40, 44, 52), 'text': (204, 204, 204), 'line_number': (136, 192, 208)},
        'atom': {'background': (39, 40, 34), 'text': (248, 248, 242), 'line_number': (165, 129, 105)},
        'vscode': {'background': (30, 30, 30), 'text': (230, 230, 230), 'line_number': (128, 128, 128)}
    }


    # Select the theme colors
    theme_colors = themes.get(theme, themes['blackandwhite'])  # Default to 'blackandwhite' if theme is not found
    background_color = theme_colors['background']
    text_color = theme_colors['text']
    line_number_color = theme_colors['line_number']

    # Load a monospace font
    font_path = "/path/to/your/font.ttf"  # Change to your font path
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
        text_width, text_height = dummy_draw.textsize(line, font=font)
        max_line_width = max(max_line_width, text_width)
        total_height += text_height + 5

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
        # Calculate leading spaces
        leading_spaces = len(line) - len(line.lstrip())
        line_number = f"{i + 1:02d} "
        draw.text((padding, y), line_number, font=font, fill=line_number_color)
        
        # Draw text line with wrapping and leading spaces
        draw.text((padding + 40 + leading_spaces * font.getsize(' ')[0], y), line.lstrip(), font=font, fill=text_color)
        y += font.getsize('A')[1] + 5  # Add spacing between lines

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

