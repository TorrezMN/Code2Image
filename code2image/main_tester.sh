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

        # Run the script with the current theme and font in editor mode
        echo "Testing theme '$THEME' with font '$FONT' in editor mode..."
        python3 -m code2image.fotetizar "$TEST_FILE" "$THEME" --font "$FONT_PATH" --mode editor
        if [ $? -ne 0 ]; then
            echo "Test failed for theme '$THEME' with font '$FONT' in editor mode."
        else
            echo "Test passed for theme '$THEME' with font '$FONT' in editor mode."
        fi

        # Run the script with the current theme and font in console mode
        echo "Testing theme '$THEME' with font '$FONT' in console mode..."
        python3 -m code2image.fotetizar "$TEST_FILE" "$THEME" --font "$FONT_PATH" --mode console
        if [ $? -ne 0 ]; then
            echo "Test failed for theme '$THEME' with font '$FONT' in console mode."
        else
            echo "Test passed for theme '$THEME' with font '$FONT' in console mode."
        fi
    done

    # Run the script without specifying a font (uses default) in editor mode
    echo "Testing theme '$THEME' with default font in editor mode..."
    python3 -m code2image.fotetizar "$TEST_FILE" "$THEME" --mode editor
    if [ $? -ne 0 ]; then
        echo "Test failed for theme '$THEME' with default font in editor mode."
    else
        echo "Test passed for theme '$THEME' with default font in editor mode."
    fi

    # Run the script without specifying a font (uses default) in console mode
    echo "Testing theme '$THEME' with default font in console mode..."
    python3 -m code2image.fotetizar "$TEST_FILE" "$THEME" --mode console
    if [ $? -ne 0 ]; then
        echo "Test failed for theme '$THEME' with default font in console mode."
    else
        echo "Test passed for theme '$THEME' with default font in console mode."
    fi
done

