import csv
import ffmpeg

'''
Put all videos in cwd into 3x2? (use variables for those) grid, with filename (no extension) overlaid in bottom left corner, zoom-style.

https://stackoverflow.com/questions/11552565/vertically-or-horizontally-stack-mosaic-several-videos-using-ffmpeg

https://github.com/kkroening/ffmpeg-python
'''

'''


this is supposedly working for the entire folder (source: https://superuser.com/questions/268985/remove-audio-from-video-file-with-ffmpeg):
FILES=/{videos_dir}/*
output_dir=/{no_audio_dir}
for input_file in $FILES
do
  file_name=$(basename $input_file)
  output_file="$output_dir/$file_name"
  ffmpeg -i $input_file -c copy -an $output_file
done

  creating 3X2 grid:
  ffmpeg -i input0.mov -i input1.mov -i input2.mov -i input3.mov -i input4.mov -i input5.mov -filter_complex "[0:v][1:v][2:v][3:v] [4:v] [5:v] xstack=inputs=6:layout=0_0|w0_0|0_h0|w0_h0|w0+w3_0|w0+w3_h0[v]" -map "[v]" 3x2grid.mp4
  creating 2X2 grid:
  ffmpeg -i input0 -i input1 -i input2 -i input3 -filter_complex "[0:v][1:v]hstack=inputs=2[top];[2:v][3:v]hstack=inputs=2[bottom];[top][bottom]vstack=inputs=2[v]" -map "[v]" output
'''

import sys
import os, os.path
import math
import ffmpeg

# TODO concat heats
# TODO add numbers
# What to do with heats 1-3 videos stylewise?
# Do into complex filters so no temp videos
# also music

# TODO need to fit all videos to common size https://superuser.com/questions/566998/how-can-i-fit-a-video-to-a-certain-size-but-dont-upscale-it-with-ffmpeg

def main():
#   Command line - python3 grid.py pathway to the folder
    heat(sys.argv[1])


def heat(folder):
    DIR = folder
    # reading in the files, likely change .mov to .mp4 but currently just testing with my .mov files
    files = [name for name in os.listdir(DIR) if name.endswith('.mov') and os.path.isfile(os.path.join(DIR, name))]

    print(files)
    # count the number of videos and call grid
    heats = math.ceil(len(files)/4)
    for i in range(0, heats):
        if i < heats-1:
            grid(files[(i*4):(i+1)*4], i)
        else:
            grid(files[i*4::], i)   
        

def grid(heatFiles, heat):
    # if there's 4 files for the heat
    if len(heatFiles) > 3:
        in0 = ffmpeg.input(heatFiles[0])
        in1 = ffmpeg.input(heatFiles[1])
        in2 = ffmpeg.input(heatFiles[2])
        in3 = ffmpeg.input(heatFiles[3])

        #Make one horizontal row
        (
            ffmpeg
            .filter([in0, in1], 'hstack')
            .output("horizontal0" + str(heat) + ".mp4")
            .run()
        )

        # #Make another horizontal row
        (
            ffmpeg
            .filter([in2, in3], 'hstack')
            .output("horizontal1" + str(heat) + ".mp4")
            .run()
        )

        # #Take the horizontal rows and put them together vertically

        in0 = ffmpeg.input("horizontal0" + str(heat) + ".mp4")
        in1 = ffmpeg.input("horizontal1" + str(heat) + ".mp4")

        (
            ffmpeg
            .filter([in0, in1], 'vstack')
            .output("grid" + str(heat) + ".mp4")
            .run()
        )
#         TODO idk what to do in terms of the style
    else:
        if len(heatFiles) == 1:
            print(heat)
        if len(heatFiles) == 2:
            print(heat)
        if len(heatFiles) == 3:
            print(heat)
# trying to print the comp numbers, problematic
    in_file = ffmpeg.input("grid" + str(heat) + ".mp4")
    (
        ffmpeg
        .drawtext(in_file, text="text", x=100, y=600, escape_text=True, fontsize = 108, box=1, boxborderw = 24, boxcolor='white')
        # .drawtext(in_file, text="text", x=200, y=500, escape_text=True, fontsize = 108, box=1, boxborderw = 24, boxcolor='white')
        # .drawtext(in_file, text="text", x=300, y=600, escape_text=True, fontsize = 108, box=1, boxborderw = 24, boxcolor='white')
        # .drawtext(in_file, text="text", x=400, y=600, escape_text=True, fontsize = 108, box=1, boxborderw = 24, boxcolor='white')
        .output('testtext100.mov')
        .run()
    ) 

if __name__ == '__main__':
    main()
