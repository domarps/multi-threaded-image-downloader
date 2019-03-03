import threading


class QueuedWorkerThread(threading.Thread):
  '''
    Abstract class.
    Every QueuedWorkerThread is a thread that
    dequeues an item from its queues and does
    some work on that item via do_work(item),
    which must be implemented by the child class.
  '''
  def __init__(self, queue):
      threading.Thread.__init__(self)
      self.q = queue

  def run(self):
      ''' When thread.start() is called, the thread calls run()
          and items on the queue begin to be processed by the thread.
      '''
      while True:
        item = self.q.get()
        if item is None:
          break
        self.do_work(item)
        self.q.task_done()

  def do_work(self, item):
    ''' Actual work done by thread on each item. Must be implemented by
        child classes.
    '''
    raise NotImplementedError

