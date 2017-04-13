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
       4 - extract the audio from video.
       5 - Save the file in the same folder with extention ".mp3".
FFMPEG flags:
    -i : input file flag
    -vn: skip video part.
    -ac: audio channels. ex: 2
    -ar: audio rate. ex: 44100
    -ab: audio bit-rate. ex: 320k
    -f: file format to use. ex: mp3
    -acodec copy: it uses the same audio stream which is already in there.
"""
import subprocess
import os
import sys

# Pre...
textfile_path = 'videos.txt'

# Read the text file
with open(textfile_path) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
files_list = [x.strip() for x in content]

# Extract audio from video.
# It already save the video file using the the named defined by output_name.
for file_num, file_path_input in enumerate(files_list, start=1):
    # Get the file name withoutextension
    file_name = os.path.basename(file_path_input)
    if 'mouthcropped' not in file_name:
        raw_file_name = os.path.basename(file_name).split('.')[0]
        file_dir = os.path.dirname(file_path_input)
        file_path_output = file_dir + '/' + raw_file_name + '.wav'
        print('processing file: %s' % file_path_input)

        # subprocess.call(
        #     ['ffmpeg', '-i', file_path_input, '-codec:a', 'libmp3lame', '-qscale:a', '2', file_path_output])
        # print('file %s saved' % file_path_output)
        subprocess.call(
            ['ffmpeg', '-i', file_path_input, '-codec:a', 'pcm_s16le', '-ac', '1', file_path_output])
        print('file %s saved' % file_path_output)

## Terminal command
# for i in **/*.mp4; do base=${i%.mp4}; ffmpeg -i $base.mp4 -codec:a pcm_s16le -ac  1 $base.wav; done
