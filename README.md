Here's a README file for your `code2image` project. It includes sections on installation, usage, and an overview of the project's purpose:

```markdown
# code2image

`code2image` is a Python tool designed to generate images from code snippets with various color themes. It is optimized for local execution, avoiding the need for online registration or services. This tool is perfect for quickly generating visual representations of code for documentation, presentations, or other purposes.

## Installation

To use `code2image`, follow these steps:

1. **Clone the Repository** (if applicable):

   ```sh
   git clone https://github.com/yourusername/code2image.git
   cd code2image
   ```

2. **Install Dependencies**:

   Ensure you have [Poetry](https://python-poetry.org/) installed. If not, you can install it using pip:

   ```sh
   pip install poetry
   ```

   Then, install the required dependencies:

   ```sh
   poetry install
   ```

   This will set up a virtual environment and install all necessary packages.

## Usage

You can use `code2image` both as a command-line tool and as a Python module. Here’s how:

### From the Console

To generate an image from a code file using `code2image` from the console, use the following command:

```sh
python3 -m code2image.code2image.fotetizar <file_path> <theme> --scenario <scenario> --font <font_path>
```

- `<file_path>`: Path to the file containing the code to draw on the image.
- `<theme>`: Color theme to use. Available themes: `monokai`, `blackandwhite`, `solarized`, `gruvbox`, `nord`, `dracula`, `github`, `one_dark`, `atom`, `vscode`.
- `<scenario>`: The scenario type for the image. Choices are `console` or `editor`.
- `<font_path>`: Path to the font file to use. Optional. If not provided, the default font will be used.

#### Example:

```sh
python3 -m code2image.code2image.fotetizar test_file.js monokai --scenario console --font path/to/your/font.ttf
```

### From Python Code

You can also use `code2image` programmatically within your Python scripts. Here’s an example:

```python
from code2image.code2image.fotetizar import new_image

text = """
def hello_world():
    print("Hello, world!")
"""

theme = "monokai"
scenario = "console"
font_path = "path/to/your/font.ttf"

new_image(scenario, text, theme, font_path)
```

This will generate an image of the code snippet with the specified theme and font.

## Project Structure

- `code2image/`: Contains the main code for generating images.
  - `fonts/`: Directory for custom fonts.
  - `code2image/`: Contains the `fotetizar.py` script and other related files.
- `tests/`: Directory for test scripts.
- `pyproject.toml`: Configuration file for Poetry.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please reach out to:

- **Author:** Milton Torrez
- **Email:** you@example.com

```

Make sure to replace placeholder values like `https://github.com/yourusername/code2image.git`, `path/to/your/font.ttf`, and `you@example.com` with the actual information for your project.
