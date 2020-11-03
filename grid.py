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

# What to do with heats 1-3 videos stylewise?
# also music

# TODO add heat#n https://stackoverflow.com/questions/22710099/ffmpeg-create-blank-screen-with-text-video?fbclid=IwAR12ySj7Ck1b3XMIKNZmlhm1-CTAxSKKq1tZhvzR_fQiYEs4m0MXoL1bqlY
# TODO need to fit all videos to common size https://superuser.com/questions/566998/how-can-i-fit-a-video-to-a-certain-size-but-dont-upscale-it-with-ffmpeg

def main():
    heat(sys.argv[1])


def heat(folder):
    DIR = folder
    # reading in the files, likely change .mov to .mp4 but currently just testing with my .mov files
    files = [name for name in os.listdir(DIR) if name.endswith('.mov') and os.path.isfile(os.path.join(DIR, name))]

    print(files)
    # count the number of videos and call grid
    heats = math.ceil(len(files)/4)
    # heats_temp = ffmpeg.input(grid(files[0: 4], 0))
    heats_temp = (grid(files[0: 4], 0))
    if heats > 0:
        for i in range(1, heats):
            if i < heats-1:
                # input files by 4 unless it's the last heat
                heats_temp = ffmpeg.concat(heats_temp, grid(files[(i*4):(i+1)*4], i))
            else:
                (   
                ffmpeg
                .concat(heats_temp, grid(files[i*4::], i))
                .output('heats.mp4')
                .run()
                )    
        
        

def grid(heatFiles, heat):
    # if there's 4 files for the heat 
    if len(heatFiles) > 3:
        in0 = ffmpeg.input(heatFiles[0])
        in1 = ffmpeg.input(heatFiles[1])
        in2 = ffmpeg.input(heatFiles[2])
        in3 = ffmpeg.input(heatFiles[3])
        # one horizontal input
        horizontal0 = ffmpeg.filter([in0, in1], 'hstack')
        # #Make another horizontal row
        horizontal1 = ffmpeg.filter([in2, in3], 'hstack')        

        # #Take the horizontal rows and put them together vertically
        gridTemp = ffmpeg.filter([horizontal0, horizontal1], 'vstack')

        # add competitor numbers
        gridText0 = ffmpeg.drawtext(gridTemp, text=(heatFiles[0].split('.')[0]), x=50, y=570, escape_text=True, fontsize = 108, box=1, boxborderw = 24, boxcolor='white')
        gridText1 = ffmpeg.drawtext(gridText0, text=(heatFiles[1].split('.')[0]), x=1200, y=570, escape_text=True, fontsize = 108, box=1, boxborderw = 24, boxcolor='white')
        gridText2 = ffmpeg.drawtext(gridText1, text=(heatFiles[2].split('.')[0]), x=50, y=1300, escape_text=True, fontsize = 108, box=1, boxborderw = 24, boxcolor='white')
        gridText3 = ffmpeg.drawtext(gridText2, text=(heatFiles[3].split('.')[0]), x=1200, y=1300, escape_text=True, fontsize = 108, box=1, boxborderw = 24, boxcolor='white')
        return gridText3

    else:
        # TODOOOOOOOO
        # Gonna give errors so keep number of files %4 to 0 otherwise the code won't run
        if len(heatFiles) == 1:
            # in0 = ffmpeg.input(heatFiles[0])
            # gridText0 = ffmpeg.drawtext(in0, text=(heatFiles[0].split('.')[0]), x=50, y=570, escape_text=True, fontsize = 108, box=1, boxborderw = 24, boxcolor='white')
            print(heat)
        if len(heatFiles) == 2:
            print(heat)
        if len(heatFiles) == 3:
            print(heat)

if __name__ == '__main__':
    main()
