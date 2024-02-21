#!/bin/bash
python3 -m compileall -b $PYFILE

# Check if the PYFILE environment variable is set
# if [ -z "$PYFILE" ]; then
#     echo "Error: PYFILE environment variable is not set."
#     exit 1
# fi

# # Compile the Python script
# output_file="${PYFILE}c"
# echo "Compiling $PYFILE ..."
# python3 -m compileall "$PYFILE" -b -x __pycache__  # Use -x to exclude __pycache__ directory
# if [ $? -eq 0 ]; then
#     echo "Compilation successful. Output file: $output_file"
# else
#     echo "Error: Compilation failed."
#     exit 1
# fi
