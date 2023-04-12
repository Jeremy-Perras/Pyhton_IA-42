class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.file = None
        self.filename = filename
        self.mode = "w+"
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.data = []
        self.sep = sep

    def __enter__(self):
        if (self.filename):
            self.file = open(self.filename, mode="r", encoding="utf-8")
            for line in self.file:
                self.data.append(
                    list(map(str.strip, line.split(self.sep))))
            if (self.file != -1):
                return self
            else:
                return None

    def __exit__(self):
        self.file.close()

    def getdata(self):
        start = self.skip_top
        end = len(self.data) - self.skip_bottom
        if self.header:
            return self.data[start + 1: end]
        else:
            return self.data[start: end]

    def getheader(self):
        return (self.data)


if (__name__ == "__main__"):
    with CsvReader("test.csv", sep=",", header=False) as file:
        if file:
            data = file.getdata()
            print(data)
            header = file.getheader()
            print(header)
        else:
            print("File is corrupted")
