# ballzoom
🕺💃

What I added to the current rescaled version: added the rescale function to the 1-3 videos per heat cases.

If I have 8(4+4):
ValueError: Encountered scale(640, 480) <1c5a59c0a8ab> with multiple outgoing edges with same upstream label None; a `split` filter is probably required

If I have 9 (4+4+1):
TypeError: Expected incoming stream(s) to be of one of the following types: ffmpeg.nodes.FilterableStream; got <class 'NoneType'>

If I have 10 videos(4+4+2):
warning that over 1000 frames duplicated, crashes

If I have 11 (4+4+3):
Input link in0:v0 parameters (size 1920x1440, SAR 9:8) do not match the corresponding output link in0:v0 parameters (1280x960, SAR 9:8)
[Parsed_concat_36 @ 0x7f819f21ac40] Failed to configure output pad on Parsed_concat_36
Error reinitializing filters!
Failed to inject frame into filter network: Invalid argument
Error while processing the decoded data for stream #13:0

