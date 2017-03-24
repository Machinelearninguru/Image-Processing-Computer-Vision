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
       4 - resize the videos to 480hd degrees clockwise.
       5 - Save the file in the same folder with prefix "front".

FFMPEG flags:

     -s <resolution> - this option will set the resolution
     -r <value> - this will set up the frame rate of a video
     -aspect <ratio> - sets the aspect ratio of the output file.
     -vcodec <codec>  - it will specify the codec to be used by FFmpeg

"""
import subprocess
import os
import sys

# Pre...
textfile_path = 'videos.txt'
output_dir_base = 'Full/Path/to/VIDEO'

# Read the text file
with open(textfile_path) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
files_list = [x.strip() for x in content]

# Transpose 90 degree & Clockwise
# It already save the video file using the the named defined by output_name.
for file_num, file_path_input in enumerate(files_list, start=1):
    # Get the file name withoutextension
    file_name = os.path.basename(file_path_input)
    ID = file_name.split('_')[1]
    raw_file_name = os.path.basename(file_name).split('.')[0]
    file_dir_input = os.path.dirname(file_path_input)
    file_dir_output = output_dir_base + '/' + ID
    if not os.path.exists(file_dir_output):
        os.makedirs(file_dir_output)
    file_path_output = file_dir_output + '/' + raw_file_name + '.mkv'
    print('processing file: %s' % file_path_input)

    subprocess.call(
        ['ffmpeg', '-y', '-i', file_path_input, '-filter_complex', 'nvresize=1:s=540x960:readback=0[out0]', '-map', '[out0]',
         '-acodec', 'copy', '-r', '30', '-vcodec', 'nvenc', '-b:v', '3M', file_path_output])
    print('file %s saved' % file_path_output)
