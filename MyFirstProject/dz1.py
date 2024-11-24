class Url:
    def __init__(self, scheme, authority, path='', query='', fragment=''):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __eq__(self, other):
        if isinstance(other, str):
            return str(self) == other
        return NotImplemented

    def __str__(self):
        url = f"{self.scheme}://{self.authority}"
        if self.path:
            url += f"/{self.path}"
        if self.query:
            url += f"?{self.query}"
        if self.fragment:
            url += f"#{self.fragment}"
        return url


class HttpsUrl(Url):
    def __init__(self, authority, path='', query='', fragment=''):
        super().__init__('https', authority, path, query, fragment)


class HttpUrl(Url):
    def __init__(self, authority, path='', query='', fragment=''):
        super().__init__('http', authority, path, query, fragment)


class GoogleUrl(Url):
    def __init__(self, path='', query='', fragment=''):
        super().__init__('https', 'google.com', path, query, fragment)


class WikiUrl(Url):
    def __init__(self, path='', query='', fragment=''):
        super().__init__('https', 'wikipedia.org', path, query, fragment)


class UrlCreator:
    def __init__(self, scheme, authority):
        self.scheme = scheme
        self.authority = authority
        self.path_parts = []
        self.query_params = {}

    def _create(self):
        path = '/'.join(self.path_parts)
        query = '&'.join(f"{k}={v}" for k, v in self.query_params.items())
        return Url(self.scheme, self.authority, path, query)

    def __getattr__(self, name):
        self.path_parts.append(name)
        return self

    def __call__(self, *args, **kwargs):
        self.path_parts.extend(args)
        self.query_params.update(kwargs)
        return self


creator = UrlCreator('http', 'google.com')
url = creator.search(q='test')._create()
print(url)

url_creator = UrlCreator(scheme='https', authority='docs.python.org')
python_url = url_creator('api', 'v1', 'list')._create()
print(python_url)

url_creator = UrlCreator(scheme='https', authority='docs.python.org')
python_url = url_creator('3').search(q='getattr', check_keywords='yes')._create()
print(python_url)