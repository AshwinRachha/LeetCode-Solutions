class Codec:
    def __init__(self):
        self.dic = dict()
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.dic:
            self.dic[longUrl] = longUrl
        return self.dic[longUrl]
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl not in self.dic:
            self.dic[shortUrl] = shortUrl
        return self.dic[shortUrl]
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))