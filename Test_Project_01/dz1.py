class Url:
    def __init__(self, scheme, authority, path, query, fragment):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __eq__(self, other):
        if isinstance(other, str):
            return str(self) == other
        return self.__dict__ == other.__dict__

    def __str__(self):
        url = f"{self.scheme}://{self.authority}"
        if self.path:
            url += self.path
        if self.query:
            url += f"?{self.query}"
        if self.fragment:
            url += f"#{self.fragment}"
        return url

class HttpsUrl(Url):
    def __init__(self, authority, path, query, fragment):
        super().__init__("https", authority, path, query, fragment)

class HttpUrl(Url):
    def __init__(self, authority, path, query, fragment):
        super().__init__("http", authority, path, query, fragment)

class GoogleUrl(Url):
    def __init__(self, path, query, fragment):
        super().__init__("https", "google.com", path, query, fragment)

class WikiUrl(Url):
    def __init__(self, path, query, fragment):
        super().__init__("https", "wikipedia.org", path, query, fragment)

url = Url("https", "example.com", "/path", "query=param", "fragment")
# print(url)  # Output: https://example.com/path?query=param#fragment

# https_url = HttpsUrl("example.com", "/path", "query=param", "fragment")
# print(https_url)  # Output: https://example.com/path?query=param#fragment

# google_url = GoogleUrl("/search", "q=python", "fragment")
# print(google_url)  # Output: https://google.com/search?q=python#fragment

print(url.str())
