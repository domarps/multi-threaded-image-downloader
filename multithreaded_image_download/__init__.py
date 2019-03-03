'''
  When we import the multithreaded_image_download package,
  python first looks here.

  For example, by including this line in __init__.py:
    `from .download_utils import URLDownloaderThread`
  we can now say:
    `from multithreaded_image_download import URLDownloaderThread`
  instead of having to always say:
    `from multithreaded_image_download.download_utils import URLDownloaderThread`.
'''
from .download_utils import URLDownloaderThread

