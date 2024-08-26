#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created on: 2024-08-25
# Author: Torrez, Milton 

import argparse
from PIL import Image, ImageDraw, ImageFont

def new_image(input_filename, scenario, text, theme, font_path):
    # Define color themes
    themes = {
        'monokai': {'background': (0, 0, 0), 'text': (255, 255, 255), 'line_number': (200, 200, 200)},
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
    for line in text.splitlines():
        text_width, text_height = dummy_draw.textsize(line if line.strip() else " ", font=font)
        max_line_width = max(max_line_width, text_width)
        total_height += text_height + 10  # Increase spacing between lines

    # Calculate image dimensions
    width = max_line_width + 60  # Adding padding for line numbers and margins
    height = total_height + 20  # Adding padding

    # Create an image with the selected background color
    image = Image.new("RGB", (width, height), background_color)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Draw text lines with line numbers
    y = padding
    for i, line in enumerate(text.splitlines()):
        # Draw line number
        line_number = f"{i + 1:02d} "
        draw.text((padding, y), line_number, font=font, fill=line_number_color)
        
        # Draw text line (handle empty lines)
        text_to_draw = line if line.strip() else " "  # Use a space for empty lines to maintain consistent height
        draw.text((padding + 40, y), text_to_draw, font=font, fill=text_color)
        _, text_height = draw.textsize(text_to_draw, font=font)
        y += text_height + 10  # Adjust spacing between lines

    # Optionally, add a border to the image
    border_color = (200, 200, 200)  # Border color remains the same
    border_width = 4
    draw.rectangle([border_width, border_width, width-border_width-1, height-border_width-1], outline=border_color)

    # Create the output file name
    output_filename = f"{input_filename.rsplit('.', 1)[0]}_{theme}.png"

    # Save the image with the new file name
    image.save(output_filename)
    print(f"Image saved as '{output_filename}'")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate an image from text with different themes.')
    parser.add_argument('file', type=str, help='The path to the file containing the text to draw on the image.')
    parser.add_argument('theme', type=str, choices=['monokai', 'blackandwhite', 'solarized', 'gruvbox', 'nord', 'dracula', 'github', 'one_dark', 'atom', 'vscode'], help='The color theme to use for the image.')
    parser.add_argument('--font', type=str, required=True, help='Path to the font file to use.')
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
    new_image(args.file, args.scenario, text, args.theme, args.font)
    print(f"Image for scenario '{args.scenario}' with theme '{args.theme}' saved as '{args.file.rsplit('.', 1)[0]}_{args.theme}.png'.")

if __name__ == "__main__":
    main()

