mkdir build
cp README.md backtick_converter.py __init.py__ test.py build
rm build.ankiaddon
zip -r build.ankiaddon build/*
