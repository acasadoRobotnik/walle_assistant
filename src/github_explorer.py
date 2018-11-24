from src.explorer import Explorer
from github import Github
import os
import base64
import requests

class GitHubExplorer(Explorer):
  def __init__(self):
    self.client = Github(os.environ['WALLE_GITHUB_TOKEN'])

  def search(self, query, receiver):

    response = "Here's what I've found on Github about '" + query + "': 🐙\n"

    for repo in self.client.get_user().get_repos():
      contents = repo.get_contents("")
      while len(contents) > 1:
        content_file = contents.pop(0)
        if content_file.path.endswith(".md"):
          decoded_content = base64.b64decode(content_file.content)
          if query in str(decoded_content):
            response += "*" + repo.full_name + "*:\n"
            response += content_file.html_url + "\n\n"

    r = requests.post(receiver, json={'text': response})


