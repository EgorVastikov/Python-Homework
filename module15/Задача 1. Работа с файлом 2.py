class SafeFile:
    def __init__(self, path, mode='w'):
        self.path = path
        self.mode = mode

    def __enter__(self):
        try:
            self.file = open(self.path, self.mode)
        except FileNotFoundError:
            self.file = open(self.path, 'w+')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        return isinstance(exc_value, (FileNotFoundError, IOError, OSError))


with SafeFile('example.txt') as f:
    f.write('hello world')
