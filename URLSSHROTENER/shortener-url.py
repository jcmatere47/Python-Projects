import pyshorteners

url = 'https://www.instagram.com/pycodebr'

s = pyshorteners.Shortener()

shortUrl = s.tinyurl.short(url)

print(f"URL Encurtada: {shortUrl}")