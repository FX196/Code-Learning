class SecureList:
    def __init__(self, data):
        self.data = data[:]  # important because we want a separate list instead of a reference to the original

    def __len__(self):
        return len(self.data)

    def __getitem__(self, position):
        return self.data.pop(position)

    def __str__(self):
        d = str(self.data)
        self.data = []
        return d

    def __repr__(self):
        return str(self)
