class URL:
    def __init__(self, scheme, authority, path, query, fragment):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment