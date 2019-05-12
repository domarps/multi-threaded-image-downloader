# multithreaded-image-downloads


If you are looking for a simple solution for multi-threaded downloads, try **aria2c**

```
sed -E 's/([^,]*),(.*)/\2\n  out=\1.jpg/' ../f8_urls.csv | aria2c -i -
```


Use this package to perform a *multi-threaded* download of a list of file URLs contained in a TSV file with lines formatted as
`<label>\t<url>\n` (separated by a single tab). Each url is downloaded to a directory with the same name as its label.

## Installation
`python setup.py install`

## Input file sample:
  In `test_URLs.tsv` (each line):
    
      `<label>\t<url>\n`

Example:
```
      fat_cat         http://farm1.staticflickr.com/1/1053148_4114c598f2.jpg
      fat_cat         http://farm2.staticflickr.com/1246/1061116668_a7e80ff2e8.jpg
      colorful_bird   http://farm1.staticflickr.com/34/100197289_ffc66e727e.jpg
      colorful_bird   http://farm2.staticflickr.com/1438/1271854268_d051bdd585.jpg
      barking_dog     http://farm1.staticflickr.com/41/103187370_7db6b95089.jpg
      barking_dog     http://farm1.staticflickr.com/45/107867809_57412c5cb4.jpg
```
## Pseudocode usage:
(complete example in `tests/test_basic.py`)
```python
  from multithreaded_image_download import URLDownloaderThread
  # define a queue and threadpool
  q = queue.Queue(maxsize=queue_size)
  threads = [URLDownloaderThread(q) for t in range(num_threads)]
  for t in threads: t.start() # begin calling run() loop, which dequeues and processes queue items
  # open a tsv file formatted like the above example
  with open('tsv_file', 'r') as f:
    for line in f:
      # read and process each line to get the item
      item = preprocess_line(line.strip().split('\t'))
      # enqueue item so that threads process it
      q.put(item) # here, item = (label_dir, file_url)
  q.join() # main thread waits for q.task_done() to be called enough times so that all enqueued elements are processed
  for i in range(queue_size): q.put(None) # make worker threads leave the t.run() loop
  for t in threads: t.join() # wait for all threads to terminate execution
  ```
  

## More info
Also, one may use this package as a skeleton to create threads that dequeue and process items from a shared python queue.
An example is provided for multithreaded image downloads, and an extended, commented usage description
is provided in tests/test_basic.py. Run the test script by calling `make test` from Terminal (tested on macOS).
