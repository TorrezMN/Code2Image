#!/bin/bash

# Define the file containing the text to draw
TEXT_FILE="script_base.py"

# Define the scenarios and themes
SCENARIOS="console editor"
THEMES="monokai blackandwhite solarized gruvbox nord"

# Loop through each scenario
for SCENARIO in $SCENARIOS; do
    # Loop through each theme
    for THEME in $THEMES; do
        echo "Testing scenario '$SCENARIO' with theme '$THEME'..."
        python3 test_from_console.py "$TEXT_FILE" "$THEME" --scenario "$SCENARIO"
    done
done

echo "All tests completed."

