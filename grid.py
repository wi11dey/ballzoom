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

def heat():
#   How many videos, call grid, grid(1) grid(2) grid(3) for i in range(4):

def grid():
  
#   input n #of heat. output grid_n.mp4
# output("grid" + str(n) + ".mp4")
#  NB!!! This could very likely be made more efficient, on command line arguments I used complex filters, not sure how to translate it into ffmpeg-python yet 
  
# Take the four competitor's videos:

# in0 = ffmpeg.input('test0.mov')
# in1 = ffmpeg.input('test1.mov')
# in0 = ffmpeg.input('test2.mov')
# in1 = ffmpeg.input('test3.mov')

# Make one horizontal row
# (
#     ffmpeg
#     .filter([in0, in1], 'hstack')
#     .output('hstack0.mov')
#     .run()
# )

# Make another horizontal row
# (
#     ffmpeg
#     .filter([in2, in3], 'hstack')
#     .output('hstack1.mov')
#     .run()
# )

# Take the horizontal rows and put them together vertically

# in0 = ffmpeg.input('hstack0.mov')
# in1 = ffmpeg.input('hstack1.mov')

# (
#     ffmpeg
#     .filter([in0, in1], 'vstack')
#     .output('grid.mov')
#     .run()
# )


# Add audio:
# input_video = ffmpeg.input('vstack.mov')

# input_audio = ffmpeg.input('testaudio.m4a')

# ffmpeg.concat(input_video, input_audio, v=1, a=1).output('audio_grid.mov').run()
    pass

def draw_comp_no():
  
#   NB! Import OS
# filename = os.path.splitext(input_file)[0]
  
#   Drawing the competitors number on the bottom left corner of the screen

#     in_file = ffmpeg.input('test1.mov')
# (
#     ffmpeg
#     .drawtext(in_file, text="294", x=100, y=600, escape_text=True, fontsize = 108, box=1, boxborderw = 24, boxcolor='white')
#     .output('testtext100.mov')
#     .run()
# ) 
     pass

if __name__ == "__main__":
    pass
