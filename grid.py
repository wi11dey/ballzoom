import csv
import ffmpeg

'''
Put all videos in cwd into 3x2? (use variables for those) grid, with filename (no extension) overlaid in bottom left corner, zoom-style.

https://stackoverflow.com/questions/11552565/vertically-or-horizontally-stack-mosaic-several-videos-using-ffmpeg

https://github.com/kkroening/ffmpeg-python
'''

'''
Raw code segments & explanation

to remove audio and save a copy of the muted video:
ffmpeg -i {INPUT VIDEO} -c copy -an {OUTPUT VIDEO}
/// -an is the audio removal



MIGHT BE IMPORTANT:
Overwrite the audio... currently only one input video, maybe use it on the grid version. (works both for cutting out singular audio track and for grid)
ffmpeg -i video.mp4 -i audio.wav -map 0:v -map 1:a -c:v copy -shortest output.mp4


this is supposedly working for the entire folder (source: https://superuser.com/questions/268985/remove-audio-from-video-file-with-ffmpeg):
FILES=/{videos_dir}/*
output_dir=/{no_audio_dir}
for input_file in $FILES
do
  file_name=$(basename $input_file)
  output_file="$output_dir/$file_name"
  ffmpeg -i $input_file -c copy -an $output_file
done



THE FOLLOWING FEW PARAGRAPHS ARE PROBS USELESS
------------------
for the numbers of the competitors:
NB! libfreetype library
https://ffmpeg.org/ffmpeg-filters.html#drawtext

2X2 drawtext (not sure if this includes creating the grid, will read up on it):
ffmpeg -i input0 -i input1 -i input2 -i input3 -filter_complex
"[0]drawtext=text='vid0':fontsize=20:x=(w-text_w)/2:y=(h-text_h)/2[v0];
 [1]drawtext=text='vid1':fontsize=20:x=(w-text_w)/2:y=(h-text_h)/2[v1];
 [2]drawtext=text='vid2':fontsize=20:x=(w-text_w)/2:y=(h-text_h)/2[v2];
 [3]drawtext=text='vid3':fontsize=20:x=(w-text_w)/2:y=(h-text_h)/2[v3];
 [v0][v1][v2][v3]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0[v]"
-map "[v]" output
-----------------




THIS IS IMPORTANT:
Add white non-transparent textbox w. black text:

ffmpeg -i test1.mov -vf "format=yuv444p, \
 drawbox=x=10:y=ih-h-10/PHI:color=white@1:width=280:height=84:t=fill, \
 drawtext=fontfile=OpenSans-Regular.ttf:text='294':fontcolor=black:fontsize=48:x=105:y=h-th-35, \
 format=yuv420p" -c:v libx264 -c:a copy -movflags +faststart testtext1.mov

  creating 3X2 grid:
  ffmpeg -i input0.mov -i input1.mov -i input2.mov -i input3.mov -i input4.mov -i input5.mov -filter_complex "[0:v][1:v][2:v][3:v] [4:v] [5:v] xstack=inputs=6:layout=0_0|w0_0|0_h0|w0_h0|w0+w3_0|w0+w3_h0[v]" -map "[v]" 3x2grid.mp4
  creating 2X2 grid:
  ffmpeg -i input0 -i input1 -i input2 -i input3 -filter_complex "[0:v][1:v]hstack=inputs=2[top];[2:v][3:v]hstack=inputs=2[bottom];[top][bottom]vstack=inputs=2[v]" -map "[v]" output
'''

'''
into Python:

Text:

ffmpeg(
.drawbox(50, 50, 120, 120, color='red', thickness=5)

)
'''


def grid():
  
    pass

if __name__ == "__main__":
    pass
