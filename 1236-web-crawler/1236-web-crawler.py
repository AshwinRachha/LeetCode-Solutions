# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        
        def getHostName(url):        
            hostname = url.split('http://')[1]
            hostname = hostname.split('.')[1]
            return hostname
        
        seen = set()
        seen.add(startUrl)
        def dfs(curr_url):
            for url in htmlParser.getUrls(curr_url):
                if url not in seen and getHostName(url) == getHostName(curr_url):
                    seen.add(url)
                    dfs(url)
        dfs(startUrl)
        return seen