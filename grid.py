import os
import ffmpeg
import argparse
import pathlib

WIDTH=1920
HEIGHT=1080

LAYOUTS=[
    ((1,   1),   ()),
    ((1,   1),   ((0, 0),)),
    ((1,   0.5), ((0, 0), (0, 1))),
    ((0.5, 0.5), ((0, 0), (0, 1), (1, 0))),
    ((0.5, 0.5), ((0, 0), (0, 1), (1, 0), (1, 1)))
]
            
def grid(recordings):
    if len(recordings) >= len(LAYOUTS):
        raise ValueError(f'No grid layout exists for {len(recordings)} recordings')

    layout = LAYOUTS[len(recordings)]

    inputs = [ffmpeg
              .input(file)
              .video
              .filter('scale', layout[0][0]*WIDTH, layout[0][1]*HEIGHT, force_original_aspect_ratio='decrease')
              .filter('pad',   layout[0][0]*WIDTH, layout[0][1]*HEIGHT, -1, -1, color='black')
              for number, file in recordings]

    if len(inputs) > 1:
        grid = ffmpeg.filter(inputs,
                             'xstack',
                             inputs=len(inputs),
                             layout="|".join(str(x*layout[0][0]*WIDTH) + '_' + str(y*layout[0][1]*HEIGHT) for x, y in layout[1]),
                             fill='black')
    else:
        grid = inputs[0]

    for recording, position in zip(recordings, layout[1]):
        number, file = recording
        x, y = position
        grid = grid.drawtext(text=number,
                             x=x*layout[0][0]*WIDTH  + 24,
                             y=y*layout[0][1]*HEIGHT + 24,
                             fontsize=108,
                             box=1,
                             boxborderw=24,
                             boxcolor='white',
                             font='Segoe UI')

    return grid.filter('pad', WIDTH, HEIGHT, -1, -1, color='black')

def heats(recordings, audio, output):
    audio_input = ffmpeg.input(audio).audio

    pathlib.Path(output).parent.mkdir(parents=True, exist_ok=True)

    j = 0
    for i in range(0, len(recordings), len(LAYOUTS) - 1):
        if len(recordings[i:i + len(LAYOUTS) - 1]) == 0:
            break
        j += 1
        grid(recordings[i:i + len(LAYOUTS) - 1]).output(audio_input, output.format(j), vsync=2).run()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate competition grids from dancer videos.')
    parser.add_argument('video', help="Directory of dancer's videos, titled like 999_Bronze_Latin.mp4")
    parser.add_argument('audio', help='Directory of competition audio, with a structure like Bronze > Latin > some_audio.mp3')
    parser.add_argument('output', help='Directory to put finished grids')
    args = parser.parse_args()

    all_recordings = {}
    for root, dirs, files in os.walk(args.video):
        for file in files:
            number, level, style, *costume = os.path.splitext(file)[0].split('_')
            all_recordings.setdefault(style, {}).setdefault(level, []).append((number, os.path.join(root, file)))

    for style, levels in all_recordings.items():
        for level, recordings in levels.items():
            heats(recordings,
                  os.path.join(args.audio, level, style, os.listdir(os.path.join(args.audio, level, style))[0]),
                  os.path.join(args.output, style, level, "heat{}.mp4"))
