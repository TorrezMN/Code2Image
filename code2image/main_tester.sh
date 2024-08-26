#!/bin/bash

# Define the directory for fonts
FONT_DIR="fonts"

# Define test parameters
THEMES="monokai blackandwhite solarized gruvbox nord dracula github one_dark atom vscode"
FONTS="UbuntuMono-BoldItalic.ttf UbuntuMono-Bold.ttf UbuntuMono-Italic.ttf UbuntuMono-Regular.ttf"

# Define the file to be tested
TEST_FILE="./tests/test_file.js"

# Loop through each theme
for THEME in $THEMES; do
    # Loop through each font
    for FONT in $FONTS; do
        # Build the full path to the font file
        FONT_PATH="$FONT_DIR/$FONT"

        # Run the script with the current theme and font
        echo "Testing theme '$THEME' with font '$FONT'..."
        python3 -m code2image.fotetizar "$TEST_FILE" "$THEME" --font "$FONT_PATH" --scenario console
        if [ $? -ne 0 ]; then
            echo "Test failed for theme '$THEME' with font '$FONT'."
        else
            echo "Test passed for theme '$THEME' with font '$FONT'."
        fi
    done
done

