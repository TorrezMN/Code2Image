#!/bin/sh

# Define the file to use for testing
test_file="test_file.js"

# Define the possible themes and scenarios
themes="monokai blackandwhite solarized gruvbox nord"
scenarios="console editor"

# Loop through each combination of theme and scenario
for theme in $themes; do
    for scenario in $scenarios; do
        echo "Testing with theme '$theme' and scenario '$scenario'..."
        python3 -m code2image.code2image.fotetizar "$test_file" "$theme" --scenario "$scenario"
        echo "Finished testing with theme '$theme' and scenario '$scenario'."
        echo "----------------------------------------"
    done
done

echo "All tests completed."

