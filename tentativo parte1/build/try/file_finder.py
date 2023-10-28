'''
The file finder has only one work, find files, no shit sherlock. But with which method? Well it requires one thing, the name of the frame.
Ones the functions has it, we can start. it has to find the PATH of the main program, and than the folder called 'build' and then 'assets',
it will return imidiately the path of the frame, and than the only thing you'll have to add which kind of assets in that frame with the normal function

'''

import os

def find_frame_assets(frame_name):
    # Get the path of the main program
    main_program_path = os.path.abspath(os.path.dirname(__file__))  # Assuming this script is in the main program directory

    print(main_program_path)

    # Construct the path to the 'build' directory
    build_directory = os.path.join(main_program_path, 'build')

    # Construct the path to the 'assets' directory within 'build'
    assets_directory = os.path.join(build_directory, 'assets')

    # Construct the path to the specific frame
    frame_path = os.path.join(assets_directory, frame_name)

    if os.path.exists(frame_path) and os.path.isdir(frame_path):
        return frame_path
    else:
        return None  # Frame not found

# Example usage
frame_name = "my_frame"
frame_assets_path = find_frame_assets(frame_name)

if frame_assets_path:
    print(f"Assets for frame '{frame_name}' are located at: {frame_assets_path}")
else:
    print(f"Frame '{frame_name}' not found.")
