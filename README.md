# Harvard Ball<i>zoom</i>

<p align="center">
 A platform for hosting ballroom online 🕺💃<br />
 <a href="https://youtu.be/aOADo7qGBds"><img src="https://i.imgur.com/5GahXea.gif" alt="Clip of Harvard Ballzoom platform" /></a>
</p>

On November 20 - November 22 2020 Harvard Ballroom Dance Team hosted their yearly competition 'Harvard Beginners', however due to the COVID-19 pandemic it was entirely virtual for the first time in the history. A big part of the competition was broadcasting the dancers' performances to continue the tradition of expressing team spirit and supporting other dancers during the event. This tool provided to be extremely helpful while managing numerous submissions of files in multiple categories and styles. 'Harvard Beginners' provided an opportunity for the team's community to stay connected during these unprecedented times and we hope this would inspire other groups or organizations to approach their events or project in a virtual way.
This piece of software allows individuals to put different videos in a custom-made grid, add music to the clips, and print names or other important information in the video. The applications of the tool are not limited to dance competition, it could also prove to be useful for music groups, or any other organization that relies on distribution of videos submitted by many different individuals.

See [here](https://youtu.be/aOADo7qGBds) for the first collegiate virtual comp!

## How to host your own!

1. Set up a system to receive video recordings from your competitors, titled like `999_Bronze_Latin.mp4`. Everything before the first underscore will be used as the competitor number, even if it contains non-digits.
1. Organize the music you want your competitors to dance to with a directory structure like
    + (root audio folder)
      + Bronze
        + Latin
          + any_file_name.mp3
        + Standard
          + music.mp3
      + Silver
        + Rhythm
          + ...

   and send the folder to your competitors to dance to. The filenames you use for the music doesn't matter: the first file found in the folder will be used as the true audio when stitching together all the videos.
1. Once you've received all your submissions titled in the form `999_Bronze_Latin.mp4`, run

   `python grid.py directory_with_submissions directory_with_music_you_sent_out output_directory`
   
   and watch the magic. You will need [Python](https://www.python.org/) and [FFmpeg](https://ffmpeg.org/) installed.
1. The code will strip all audio from dancer's videos, stitch them into grids, and overlay the original audio over all of them. The output directory will be structured like
    + (root output folder)
      + Latin
        + Newcomer
          + heat1.mp4
        + Silver
          + heat1.mp4
          + heat2.mp4
      + Rhythm
        + ...

   so the announcers can broadcast each one at their pace. See [https://youtu.be/aOADo7qGBds](https://youtu.be/aOADo7qGBds) for an example of a successful comp.

_from Will Dey and Angelika Antsmäe, Harvard Class of 2023_
