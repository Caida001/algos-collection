TinyURL is a URL shortening service where you enter a URL such as
https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no
restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.



import random

class Codec:
    def __init__(self):
      self.longToShort = {}
      self.shortToLong = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        characters = string.ascii_letters + "0123456789"

        while longUrl not in self.longToShort:
          short = ''.join(random.choice(characters) for _ in range(6))
          if short not in self.shortToLong:
            self.longToShort[longUrl] = short
            self.shortToLong[short] = longUrl

        return 'http://tinyurl.com/' + self.longToShort[longUrl]


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.shortToLong[shortUrl.split('/')[-1]]
