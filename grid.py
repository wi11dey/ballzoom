import sys
import os, os.path
import math
import ffmpeg


# What to do with heats 1-3 videos stylewise?


def main():
    heat(sys.argv[1])


def heat(folder):
    DIR = folder
    # reading in the files, likely change .mov to .mp4 but currently just testing with my .mov files
    files = [name for name in os.listdir(DIR) if name.endswith('.mov') and os.path.isfile(os.path.join(DIR, name))]
    audioFile = [name for name in os.listdir(DIR) if name.endswith('.m4a') and os.path.isfile(os.path.join(DIR, name))]
    print(files)
    # count the number of videos and call grid
    heats = math.ceil(len(files)/4)
    # heats_temp = ffmpeg.input(grid(files[0: 4], 0))
    heats_temp = (grid(files[0: 4], 0, audioFile[0]))
    if heats > 0:
        for i in range(1, heats):
            if i < heats-1:
                # input files by 4 unless it's the last heat
                heats_temp = ffmpeg.concat(heats_temp, grid(files[(i*4):(i+1)*4], i, audioFile[0]))
            else:
                (   
                ffmpeg
                .concat(heats_temp, grid(files[i*4::], i, audioFile[0]))
                .output('heats.mp4')
                .run()
                )    
        
        

def grid(heatFiles, heat, audioFile):
    # if there's 4 files for the heat 
    if len(heatFiles) > 3:
        in0 = ffmpeg.input(heatFiles[0])
        in1 = ffmpeg.input(heatFiles[1])
        in2 = ffmpeg.input(heatFiles[2])
        in3 = ffmpeg.input(heatFiles[3])
        gridTemp = ffmpeg.filter([in0, in1, in2, in3], 'xstack', inputs=4, layout='0_0|0_h0|w0_0|w0_h0')
        # add competitor numbers
        gridText0 = ffmpeg.drawtext(gridTemp, text=(heatFiles[0].split('.')[0]), x=50, y=570, escape_text=True, fontsize = 108, box=1, boxborderw = 24, boxcolor='white')
        gridText1 = ffmpeg.drawtext(gridText0, text=(heatFiles[1].split('.')[0]), x=1200, y=570, escape_text=True, fontsize = 108, box=1, boxborderw = 24, boxcolor='white')
        gridText2 = ffmpeg.drawtext(gridText1, text=(heatFiles[2].split('.')[0]), x=50, y=1300, escape_text=True, fontsize = 108, box=1, boxborderw = 24, boxcolor='white')
        gridText3 = ffmpeg.drawtext(gridText2, text=(heatFiles[3].split('.')[0]), x=1200, y=1300, escape_text=True, fontsize = 108, box=1, boxborderw = 24, boxcolor='white')
        rescaledGrid = ffmpeg.filter(gridText3, 'scale', size='hd1080', force_original_aspect_ratio='increase')
        audioInput = ffmpeg.input(audioFile)
        gridAudio = ffmpeg.concat(rescaledGrid, audioInput, v=1, a=1)
        return gridAudio

    else:
        # TODOOOOOOOO
        # Gonna give errors so keep number of files %4 to 0 otherwise the code won't run
        if len(heatFiles) == 1:
            in0 = ffmpeg.input(heatFiles[0])
            gridText0 = ffmpeg.drawtext(in0, text=(heatFiles[0].split('.')[0]), x=50, y=570, escape_text=True, fontsize = 108, box=1, boxborderw = 24, boxcolor='white')
            rescaledGrid = ffmpeg.filter(gridText0, 'scale', size='hd1080', force_original_aspect_ratio='increase')
            audioInput = ffmpeg.input(audioFile)
            gridAudio = ffmpeg.concat(rescaledGrid, audioInput, v=1, a=1)
            return gridAudio

        if len(heatFiles) == 2:

            in0x = ffmpeg.input(heatFiles[0])
            in0= ffmpeg.filter(in0x, 'scale', size='hd1080', force_original_aspect_ratio='increase')
            in1x = ffmpeg.input(heatFiles[1])
            in1 = ffmpeg.filter(in1x, 'scale', size='hd1080', force_original_aspect_ratio='increase')
            in2x = ffmpeg.input('black2.png')
            in2 = ffmpeg.filter(in2x, 'scale', size='hd1080', force_original_aspect_ratio='increase')
            in3x = ffmpeg.input('black2.png')
            in3 = ffmpeg.filter(in3x, 'scale', size='hd1080', force_original_aspect_ratio='increase')

            

            horizontal0 = ffmpeg.filter([in0, in1], 'hstack')
            # #Make another horizontal row
            horizontal1 = ffmpeg.filter([in2, in3], 'hstack')        

            # #Take the horizontal rows and put them together vertically
            gridTemp = ffmpeg.filter([horizontal0, horizontal1], 'vstack')

            # add competitor numbers
            gridText0 = ffmpeg.drawtext(gridTemp, text=(heatFiles[0].split('.')[0]), x=50, y=570, escape_text=True, fontsize = 108, box=1, boxborderw = 24, boxcolor='white')
            gridText1 = ffmpeg.drawtext(gridText0, text=(heatFiles[1].split('.')[0]), x=1200, y=570, escape_text=True, fontsize = 108, box=1, boxborderw = 24, boxcolor='white')
            # gridText2 = ffmpeg.drawtext(gridText1, text=(heatFiles[2].split('.')[0]), x=50, y=1300, escape_text=True, fontsize = 108, box=1, boxborderw = 24, boxcolor='white')
            # gridText3 = ffmpeg.drawtext(gridText2, text=(heatFiles[3].split('.')[0]), x=1200, y=1300, escape_text=True, fontsize = 108, box=1, boxborderw = 24, boxcolor='white')
            rescaledGrid = ffmpeg.filter(gridText1, 'scale', size='hd1080', force_original_aspect_ratio='increase')
            audioInput = ffmpeg.input(audioFile)
            gridAudio = ffmpeg.concat(rescaledGrid, audioInput, v=1, a=1)
            return gridAudio
        
        if len(heatFiles) == 3:
            print(heat)

if __name__ == '__main__':
    main()
