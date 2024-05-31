from googlesearch import search

from serving.adapter import Adapter

class SearchAdapter(Adapter):
    def __init__(self):
        pass
    def connect(self, on_connect):
        pass

    def search(self, query):
        return search(query, tld="com", num=10, stop=10, pause=2)
        