#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created on: 2024-08-25
# Author: Torrez, Milton 


from PIL import Image, ImageDraw, ImageFont

# Create an image with a black background
width, height = 800, 400
background_color = (0, 0, 0)
image = Image.new("RGB", (width, height), background_color)

# Load a monospace font
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
font_size = 20
font = ImageFont.truetype(font_path, font_size)

# Create a drawing object
draw = ImageDraw.Draw(image)

# Define text color and position
text_color = (0, 255, 0)  # Green color for the console text
line_number_color = (255, 255, 255)  # White color for the line numbers
text_position = (10, 10)  # Starting position for the text

# Calculate line height using getbbox
line_height = font.getbbox("A")[3] - font.getbbox("A")[1] + 5

# Add console-like text with line numbers
console_text = """
user@linux:~$ ls
Desktop  Documents  Downloads  Music  Pictures  Videos
user@linux:~$ echo 'Hello, World!'
Hello, World!
user@linux:~$
"""
lines = console_text.strip().split("\n")
for i, line in enumerate(lines):
    # Draw line number
    line_number = f"{i + 1:02d} "
    draw.text((text_position[0], text_position[1] + i * line_height), line_number, font=font, fill=line_number_color)
    
    # Draw text line
    draw.text((text_position[0] + 40, text_position[1] + i * line_height), line, font=font, fill=text_color)

# Optionally, add a border to the image
border_color = (200, 200, 200)
border_width = 4
draw.rectangle([border_width, border_width, width-border_width-1, height-border_width-1], outline=border_color)

# Save the image
image.save("linux_console_with_line_numbers.png")

