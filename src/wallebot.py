from src.github_explorer import GitHubExplorer

from multiprocessing import Process, Queue, cpu_count
from bottle import run,post,request,response,route
import os
import urllib



class WalleBot(object):
  def __init__(self):
      self.github_explorer = GitHubExplorer()
      self.queue = Queue()
      self.nb_workers = cpu_count()

      for i in range(self.nb_workers):
        msg_puller_process = Process(target=self.pull_msgs, args=[self.queue])
        msg_puller_process.start()

  def find_docs(self):
    postdata = request.forms.get("text")
    receiver = request.forms.get("response_url")
    package = {"response_type": "in_channel", "text": "{}".format(postdata)}
    response.content_type = 'application/json'
    self.queue.put((postdata, receiver))
    return "I'm working on it..."

  def search_on_github(self, *args):
    return self.github_explorer.search(args[0], args[1])

  def pull_msgs(self, queue):
    while True:
        msg, receiver = queue.get()
        if msg is None:
            break
        self.search_on_github(msg, receiver)

if __name__ == '__main__':
  walle = WalleBot()
  route("/find", method='post')(walle.find_docs)

  port_config = int(os.getenv('PORT', 5000))
  run(host='0.0.0.0', port=port_config)

