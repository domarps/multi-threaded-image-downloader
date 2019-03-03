'''
Use this file to download a list of files with lines formatted as
<label>\t<url>\n (a single tab) to directories with same names as labels.

Example:
  test_URLs.tsv:
    Each line: <label>\t<url>\n
    Example:
    fat_cat         http://farm1.staticflickr.com/1/1053148_4114c598f2.jpg
    fat_cat         http://farm2.staticflickr.com/1246/1061116668_a7e80ff2e8.jpg
    colorful_bird   http://farm1.staticflickr.com/34/100197289_ffc66e727e.jpg
    colorful_bird   http://farm2.staticflickr.com/1438/1271854268_d051bdd585.jpg
    barking_dog     http://farm1.staticflickr.com/41/103187370_7db6b95089.jpg
    barking_dog     http://farm1.staticflickr.com/45/107867809_57412c5cb4.jpg
'''
import os
import queue
import progressbar
from .context import multithreaded_image_download
from multithreaded_image_download import URLDownloaderThread

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_download(self):
        ''' Test downloading images in parallel from tests/test_URLs.tsv. '''

        # Specify threading and queue settings.
        num_threads = 16 # number of image downloads in parallel
        qsize = 256 # maximum number of URLs to put on the queue
        q = queue.Queue(maxsize=qsize)

        # Create threads to run image downloads.
        print('Creating threads...')
        threads = []
        for i in range(num_threads):
          t = URLDownloaderThread(q)
          t.start()  # calls t.run()
          threads.append(t)

        # Load URLs from file.
        url_file = 'tests/test_URLs.tsv'
        data_dest = 'tests/test_downloaded_images' # folder where image directories will be created
        bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)

        # Put URLs in queue so that threads can grab URLs to download.
        print('Downloading images...')
        downloads = 0
        with open(url_file, 'r') as f:
          for line in f:
            label, url = line.strip().split('\t')
            destination_dir = os.path.join(data_dest, label)
            if not os.path.isdir(destination_dir):
              os.makedirs(destination_dir) # recursively create nested dirs
            q.put((url, destination_dir))
            bar.update(downloads)
            downloads += 1

        # Wait for all threads to finish and queue to become empty.
        q.join()
        for i in range(qsize):
          q.put(None)
        for t in threads:
          t.join()

        print('\nFinished.')
        n = len(open(url_file, 'r').readlines())
        assert downloads == n, \
          'Number of urls saved does not match length of URLs file.'


if __name__ == '__main__':
  unittest.main()


