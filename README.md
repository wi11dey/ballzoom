# ballzoom
🕺💃

What I added to the current rescaled version: added the rescale function to the 1-3 videos per heat cases.


If all the same size:
8
works :)
9
Input link in0:v0 parameters (size 1440x1080, SAR 0:1) do not match the corresponding output link in0:v0 parameters (1280x960, SAR 9:8)
[Parsed_concat_33 @ 0x7fa269a1f880] Failed to configure output pad on Parsed_concat_33
Error reinitializing filters!
Failed to inject frame into filter network: Invalid argument
Error while processing the decoded data for stream #12:0

10
works but adds videos horizontally (black line horizontal, fix...)
:)

11
 Input link in0:v0 parameters (size 1440x1080, SAR 9:8) do not match the corresponding output link in0:v0 parameters (1280x960, SAR 9:8)
[Parsed_concat_33 @ 0x7fdb4d0428c0] Failed to configure output pad on Parsed_concat_33
Error reinitializing filters!
Failed to inject frame into filter network: Invalid argument
Error while processing the decoded data for stream #12:0




If different scales:

More than 1000 frames duplicated.
 Frame rate very high for a muxer not efficiently supporting it.
Please consider specifying a lower framerate, a different muxer or -vsync 2
[libx264 @ 0x7fd4a700de00] using SAR=9/8
[libx264 @ 0x7fd4a700de00] MB rate (4800000000) > level limit (16711680)

