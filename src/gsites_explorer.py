from src.explorer import Explorer
import os
import base64
import requests
import gdata.sites.client
import gdata.sites.data


class GSitesExplorer(Explorer):
    def __init__(self):

        SCOPE = 'https://sites.google.com/feeds/'

        auth2token = gdata.gauth.OAuth2Token(client_id=os.environ['WALLE_G_CLIENT'],
                                             client_secret=os.environ['WALLE_G_SECRET'],
                                             scope=SCOPE,
                                             user_agent='sites-test/1.0')

        print("setting up client")

        self.client = gdata.sites.client.SitesClient(source='sites-test',
                                                     site='robotnik.es',
                                                     domain='robotnik.es',
                                                     auth_token=auth2token)

        auth2token.authorize(self.client)

        print("authorized")

    def search(self, query, receiver):
        feed = self.client.GetSiteFeed()

        response = ""

        for entry in feed.entry:
            print('%s [%s]' % (entry.title.text, entry.Kind()))
            response += '%s [%s]' % (entry.title.text, entry.Kind())

        r = requests.post(receiver, json={'text': response})
