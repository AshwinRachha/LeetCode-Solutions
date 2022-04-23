class Codec:
    def __init__(self):
        self.dic = dict()
        self.counter = 0
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.dic[self.counter] = longUrl
        self.counter+=1
        print(self.dic)
        return 'http://tinyurl.com/' + str(self.counter-1)
    
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        index = shortUrl.split('/')[-1]
        return self.dic[int(index)]
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))