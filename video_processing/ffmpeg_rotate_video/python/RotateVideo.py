"""
The subprocess module provides an interface to working with additional processes. It offers a higher-level
interface than some of the other available modules. It is intended to replace functions such as os.system().
In this code it is used to rotate a video file with the support of "ffmpeg" by the ubuntu.

The reason behind using python rather than command line is its higher flexibility to dig into file paths and
doing further processes online.

This python module:

       1 - Read a text file which directs to video files paths.
       2 - Make a list of those paths.
       3 - Read the list files one by one.
       4 - Rotate each video 90 degrees clockwise.
       5 - Save the file in the same folder with prefix "front".
"""
import subprocess
import os

# Pre...
textfile_path = 'videos.txt'
output_prefix = 'front'

# Read the text file line by line.
with open(textfile_path) as f:
    content = f.readlines()

# Remove whitespace characters like `\n` at the end of each line
files_list = [x.strip() for x in content]

# Transpose 90 degree & Clockwise
# It already save the video file using the the named defined by output_name.
for file_num, file_path in enumerate(files_list, start=1):

    # Get the file name with extension
    file_name = os.path.basename(file_path)

    # Get the file name without extension
    raw_file_name = os.path.basename(file_name).split('.')[0]

    # Get the input file directory path.
    file_dir = os.path.dirname(file_path)

    # Form the output file full path.
    output_file_path = file_dir + '/' + output_prefix + '_' + raw_file_name + '.mov'

    print('processing file: %s' % file_path)
    subprocess.call(
        ['ffmpeg', '-i', file_path, '-vf', 'transpose=1', '-vcodec', 'nvenc', '-preset', 'slow', '-b:v', '5M',
         '-acodec', 'copy', output_file_path])
    print('file %s saved' % output_file_path)
