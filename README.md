# How to turn a sequence of still images (OpenEXR) into a movie, using Python and ffmpeg.

# Self Description
I am Masataka @plinecom, a pipeline engineer at digitalbigmo Inc.

# What is this?
I was asked to make a QuickTime movie (.mov) for each folder of tens of thousands of still image OpenEXR files in about 1000 folders. It would be too much trouble if I had to use compositing software to composite each one, so I decided to use Python to control ffmpeg and process it.

# For now, here's the code
```python:main.py
import ffmpeg
import glob


if __name__ == '__main__':

    for path in glob.glob('/foo/bar/*'):
        print(path)
        fname = path.split('/')[-1].
        print(fname)
        video = ffmpeg.input(path + '/*.exr',
                             pattern_type='glob',
                             framerate=24
                             ).output('/foo/bar/' + fname + '.mov',
                                      pix_fmt='yuv420p'
                                      ).run(overwrite_output=True)
```

# Required Python external modules.
* ffmpeg-python
```terminal:terminal
pip install ffmpeg-python
```
Download it from PyPI using pip. This module does not include ffmpeg itself, so you need to install it using a package management system such as brew, or download ffmpeg and ffprobe, which are pre-built for each platform, from the official ffmpeg website and put them in a directory where the path goes. Dockerfile should also be prepared.
I also prepared a Dockerfile.
```Dockerfile:Dockerfile
FROM rockylinux:8
RUN dnf install -y which python3 epel-release
RUN dnf config-manager --set-enabled powertools
RUN dnf localinstall -y --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm
RUN dnf install -y ffmpeg
RUN pip3 install ffmpeg-python
```
```terminal:terminal
docker pull plinecom/py_exr_ffmpeg
```

# Code description

This time, we don't have to do anything because of OpenEXR, so you should be able to turn a PNG, TIFF, or DPX still image into a movie. ffmpeg is a good guy.
## Instructions on how to read EXR files
```python:
    video = ffmpeg.input(path + '/*.exr',
                         pattern_type='glob',
                         framerate=24
```
The wildcard is in the path name to tell it to glob and that the frame rate is 24p this time. It would be elegant to process the frame rate by extracting the timecode from the OpenEXR header, but if the person in charge can figure it out, that's fine.


## Instructions on how to export video.
```python:
                             ).output('/foo/bar/' + fname + '.mov',
                                      pix_fmt='yuv420p'
```
Specify the destination and file name. As a bonus, pix_fmt is indicated. If pix_fmt is not set to 'yuv420p', a file which cannot be previewed on mac will be created. It is inconvenient for a simple check use, so I'll put up with it and set it to 4:2:0. By the way, I am not instructing you to export at the very small size of 420p, I am instructing you how to express the colors.

https://qiita.com/mriho/items/a16b3c618c378efeb58f

## Instructions on how to process
```python:
                                      ).run(overwrite_output=True)
```
If there is already a video file with the same name, we have a problem with it stopping, so we instruct it to force overwrite. If there is nothing special like that, just run() is fine.

# advertisement
digitalbigmo Inc. sells beautiful skin plug-ins and provides video VFX production services. If you are interested, please visit our web page. Let's work together.

https://digitalbigmo.com

# References
[ffmpeg main home (English)](https://ffmpeg.org/)

https://kkroening.github.io/ffmpeg-python/
