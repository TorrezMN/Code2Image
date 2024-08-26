#!/bin/bash

# Define the fonts directory and test file paths
FONTS_DIR="code2image/fonts"
TEST_FILE="tests/test_file.js"

# List of themes and fonts to test
THEMES=("monokai" "blackandwhite" "solarized" "gruvbox" "nord" "dracula" "github" "one_dark" "atom" "vscode")
FONTS=("UbuntuMono-BoldItalic.ttf" "UbuntuMono-Bold.ttf" "UbuntuMono-Italic.ttf" "UbuntuMono-Regular.ttf")

# Function to run the test
run_test() {
    local theme=$1
    local font=$2
    local font_path="$FONTS_DIR/$font"
    local output_file="output_${theme}_${font}.png"

    echo "Testing theme '$theme' with font '$font'..."

    # Run the code2image command using Poetry
    poetry run code2image "$TEST_FILE" "$theme" --scenario console --font "$font_path"

    if [ $? -eq 0 ]; then
        echo "Test completed successfully. Output file: $output_file"
    else
        echo "Test failed for theme '$theme' with font '$font'."
    fi
}

# Run tests for each combination of theme and font
for theme in "${THEMES[@]}"; do
    for font in "${FONTS[@]}"; do
        run_test "$theme" "$font"
    done
done

