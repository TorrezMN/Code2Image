#!/bin/sh

# Define the file to test and the scenarios
FILE="test_file.js"
SCENARIOS="console editor"
THEMES="blackandwhite solarized gruvbox nord dracula github one_dark atom vscode"

# Check if the file exists
if [ ! -f "$FILE" ]; then
  echo "Error: File '$FILE' not found!"
  exit 1
fi

# Loop through scenarios and themes to run the tests
for SCENARIO in $SCENARIOS; do
  for THEME in $THEMES; do
    echo "Testing scenario '$SCENARIO' with theme '$THEME'..."
    python3 -m code2image.code2image.fotetizar "$FILE" "$THEME" --scenario "$SCENARIO"
    
    # Check if the command was successful
    if [ $? -eq 0 ]; then
      echo "Success: '$SCENARIO' with '$THEME' theme."
    else
      echo "Error: Failed to generate image for '$SCENARIO' with '$THEME' theme."
    fi
  done
done

