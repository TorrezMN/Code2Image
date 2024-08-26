import os
from PIL import Image, ImageDraw, ImageFont

# Define color themes
THEMES = {
    "monokai": {"background": (39, 40, 34), "text": (248, 248, 242), "line_number": (128, 128, 128)},
    "blackandwhite": {"background": (255, 255, 255), "text": (0, 0, 0), "line_number": (128, 128, 128)},
    "solarized": {"background": (0, 43, 54), "text": (131, 148, 150), "line_number": (108, 113, 122)},
    "gruvbox": {"background": (40, 40, 40), "text": (235, 219, 178), "line_number": (160, 113, 24)},
    "nord": {"background": (46, 52, 64), "text": (216, 222, 233), "line_number": (136, 192, 208)},
    "dracula": {"background": (40, 42, 54), "text": (248, 248, 242), "line_number": (98, 114, 164)},
    "github": {"background": (255, 255, 255), "text": (36, 41, 46), "line_number": (199, 199, 199)},
    "one_dark": {"background": (40, 44, 52), "text": (171, 178, 191), "line_number": (106, 115, 125)},
    "atom": {"background": (33, 37, 43), "text": (171, 178, 191), "line_number": (109, 130, 143)},
    "vscode": {"background": (30, 30, 30), "text": (212, 212, 212), "line_number": (128, 128, 128)},
    "commodore64": {"background": (66, 77, 72), "text": (152, 219, 160), "line_number": (255, 255, 255)},  # Custom theme for Commodore64 mode
}

def render_image(input_file, theme, font_path=None, mode="editor"):
    # Determine the default font directory and default font path
    default_font_dir = os.path.join(os.path.dirname(__file__), '../fonts')
    default_font_path = os.path.join(default_font_dir, 'UbuntuMono-Regular.ttf')

    # Use the provided font or fallback to the default font
    if font_path and os.path.exists(font_path):
        font = ImageFont.truetype(font_path, size=14)  # Adjust size as needed
        line_number_font = ImageFont.truetype(font_path, size=14)  # Same size for line numbers
    else:
        font = ImageFont.truetype(default_font_path, size=14)  # Adjust size as needed
        line_number_font = ImageFont.truetype(default_font_path, size=14)  # Same size for line numbers

    # Load the input file
    with open(input_file, 'r') as f:
        code = f.read()

    # Get the selected theme colors
    theme_colors = THEMES.get(theme, THEMES["monokai"])
    background_color = theme_colors["background"]
    text_color = theme_colors["text"]
    line_number_color = theme_colors["line_number"]

    # Adjust font and image size for console mode
    if mode == "console":
        font = ImageFont.truetype(font_path or default_font_path, size=18)
        line_number_font = ImageFont.truetype(font_path or default_font_path, size=18)

    # Calculate the image size based on the code's content
    lines = code.split('\n')
    max_line_length = max([len(line) for line in lines])
    image_width = max_line_length * 10 + 40  # 10 is an approximate character width in pixels
    image_height = len(lines) * 18 + 40  # 18 is an approximate line height in pixels; added 40px for header

    if mode == "console":
        image_height += 20  # Add some extra space for console mode

    # Create a new image with the calculated size and background color
    img = Image.new('RGB', (image_width, image_height), color=background_color)
    d = ImageDraw.Draw(img)

    if mode == "editor":
        # Draw the header background
        header_height = 30
        header_background_color = (50, 50, 50)  # Darker shade for header background
        d.rectangle([(0, 0), (image_width, header_height)], fill=header_background_color)

        # Draw the three circles for window control buttons
        circle_radius = 7
        circle_positions = [(20, 15), (40, 15), (60, 15)]
        circle_colors = [(255, 95, 86), (255, 189, 46), (39, 201, 63)]  # Close, Minimize, Maximize colors
        for pos, color in zip(circle_positions, circle_colors):
            d.ellipse([(pos[0] - circle_radius, pos[1] - circle_radius),
                       (pos[0] + circle_radius, pos[1] + circle_radius)],
                      fill=color)

    # Draw the line numbers and code text on the image
    line_number_width = 30  # Width reserved for line numbers
    x_text = line_number_width + 10  # Padding after line numbers
    y_text_start = 40 if mode == "editor" else 10  # Adjust the starting position for text

    for i, line in enumerate(lines):
        # Draw line number
        line_number_text = f"{i + 1}"
        d.text((10, y_text_start + i * 18), line_number_text, font=line_number_font, fill=line_number_color)
        
        # Draw code text
        d.text((x_text, y_text_start + i * 18), line, font=font, fill=text_color)

    # Save the image in the current directory with the theme name and input file name
    mode_suffix = "_console" if mode == "console" else ""
    output_file = f"{os.path.splitext(os.path.basename(input_file))[0]}_{theme}{mode_suffix}.png"
    img.save(output_file)
    print(f"Image saved as {output_file}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("theme", help="Theme to use for rendering")
    parser.add_argument("--font", help="Optional custom font file to use", default=None)
    parser.add_argument("--mode", help="Scenario type (console or editor)", default="editor")

    args = parser.parse_args()

    render_image(args.input_file, args.theme, args.font, args.mode)

