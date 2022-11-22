import ffmpeg
import glob

if __name__ == '__main__':

    for path in glob.glob('/foo/bar/*'):
        print(path)
        fname = path.split('/')[-1]
        print(fname)
        video = ffmpeg.input(path + '/*.exr',
                             pattern_type='glob',
                             framerate=24
                             ).output('/for/bar/' + fname + '.mov',
                                      pix_fmt='yuv420p'
                                      ).run(overwrite_output=True)

