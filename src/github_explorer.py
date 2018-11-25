from src.explorer import Explorer
from github import Github
import os
import base64
import requests

class GitHubExplorer(Explorer):
  def __init__(self, org):
    self.client = Github(os.environ['WALLE_GITHUB_TOKEN'])
    self.organization = org

  def search(self, query, receiver):

    response = ""

    for repo in self.client.get_organization(self.organization).get_repos():
      contents = repo.get_contents("")
      while len(contents) > 1:
        content_file = contents.pop(0)
        if content_file.path.endswith(".md"):
          decoded_content = base64.b64decode(content_file.content)
          if query in str(decoded_content):
            response += "*" + repo.full_name + "*:\n"
            response += content_file.html_url + "\n\n"

    if len(response) == 0:
      response = self.no_luck_msg(query, 'GitHub')
    else:
      response = self.success_msg(query, 'GitHub') + "\n" + response

    r = requests.post(receiver, json={'text': response})


