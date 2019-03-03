import os
import urllib.request

from . import thread_utils


class URLDownloaderThread(thread_utils.QueuedWorkerThread):
  '''
    Every URLDownloaderThread is a thread that
    repeatedly dequeues an item from self.queue
    and calls do_work(item).
  '''
  def __init__(self, queue):
      ''' Optional method included for clarity if not passing new
          args or changing self.
      '''
      super().__init__(queue)

  def do_work(self, item):
      ''' When this thread dequeues an item, it processes it by calling
          do_work(item). Must be overridden.
      '''
      self.download(item)

  def download(self, item):
      ''' Unwraps a dequeued item and performs the download from a url to
          a specific directory.
       '''
      from_url, to_dir = item
      download(from_url, to_dir)

def download(from_url, to_dir):
    ''' Download data at a url to a specific directory. '''
    try:
      fname = os.path.basename(from_url)
      to_path = os.path.join(to_dir, fname)
      if not os.path.isfile(to_path):
        if not os.path.isdir(to_dir):
          os.makedirs(to_dir) # recursively create nested dirs
        urllib.request.urlretrieve(from_url, to_path)
    except Exception as e:
      print('ERROR:', e, type(e).__name__)

