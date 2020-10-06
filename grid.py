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

this is supposedly working for the entire folder (source: https://superuser.com/questions/268985/remove-audio-from-video-file-with-ffmpeg):
FILES=/{videos_dir}/*
output_dir=/{no_audio_dir}
for input_file in $FILES
do
  file_name=$(basename $input_file)
  output_file="$output_dir/$file_name"
  ffmpeg -i $input_file -c copy -an $output_file
done

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


Just creating the 2X2 grid:

ffmpeg -i input0 -i input1 -i input2 -i input3 -filter_complex "[0:v][1:v]hstack=inputs=2[top];[2:v][3:v]hstack=inputs=2[bottom];[top][bottom]vstack=inputs=2[v]" -map "[v]" output
  
'''
def grid():
    pass

if __name__ == "__main__":
    pass
