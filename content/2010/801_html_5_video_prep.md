Title: HTML 5 Video Prep
Date: 2010-05-04 17:13:00
Tags: imported
Category: 
Slug: html_5_video_prep

<div style="margin: 15px; float: right"><a href="http://www.flickr.com/photos/36983395@N00/513636061/" title="HTML5 fist, after A List Apart" target="_blank"><img src="http://farm1.static.flickr.com/191/513636061_98d07f7966_m.jpg" alt="HTML5 fist, after A List Apart" border="0" /></a><small><a href="http://creativecommons.org/licenses/by/2.0/" title="Attribution License" target="_blank"><img src="http://blog.mcstudios.net/wordpress/wp-content/plugins/photo-dropper/images/cc.png" alt="Creative Commons License" border="0" width="16" height="16" align="absmiddle" /></a> <a href="http://www.photodropper.com/photos/" target="_blank">photo</a> credit: <a href="http://www.flickr.com/photos/36983395@N00/513636061/" title="justinsomnia" target="_blank">justinsomnia</a></small></div>So what caused me to be up till 2 in the morning? Struggling with video encoding, conversion and HTML5 fickleness.  Essentially, this is not a process for mere mortals.  While video in general is complicated enough, most will and should rely on a site like youtube to share their videos (at least basic creators).  However due to certain, ummm... how shall we say, "ambitious" music labels, music video remixes get flagged and punted immediately.  It will be nice if we can get a universally supported video codec (stay tuned for Google I/O) as it will greatly streamline this process (or should in theory).

I learned recently that Handbrake has let it's ogg/theora capability go stale and will not bring it back.  Additionally, my video editor of choice, <a href="http://www.kdenlive.org/">kdenlive</a> doesn't generate web optimized mp4 files (where the index is at the beginning of the file).  Thus, after rendering I struggled a bit to find a combination of programs that would generate the necessary ogv and mp4 videos to support the html5 video browser ecosystem.  Here's what I came up with... Modify to suit your needs.

<h4>HandBrakeCLI</h4>

<code>HandBrakeCLI -i input.mp4 -o output.mp4 --encoder x264 --vb 2000 --ab 128 --width x --height y --crop 0:0:0:0 --optimize</code>

<h4>ffmpeg2theora</h4>

<code>ffmpeg2theora -V 2000 input.mp4 #generates input.ogv</code>

It also doesn't help that ubuntu has <a href="https://bugs.launchpad.net/ubuntu/+source/ffmpeg-debian/+bug/6366">decided</a> it can't ship an ffmpeg with aac support (which means I have to modify kdenlive's profile.xml to use libmp3lame instead).
