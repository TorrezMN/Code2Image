
rm -rf dist/
poetry version patch
poetry publish --build
