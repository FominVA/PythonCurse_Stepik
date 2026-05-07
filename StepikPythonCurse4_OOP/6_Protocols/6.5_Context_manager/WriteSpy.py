class WriteSpy:

    def __init__(self, file1, file2, to_close=False):
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.to_close:
            self.file1.close()
            self.file2.close()
        return False

    def write(self, text):
        try:
            f1_writable = self.file1.writable()
        except ValueError:
            raise ValueError("Файл закрыт или недоступен для записи") from None
        try:
            f2_writable = self.file2.writable()
        except ValueError:
            raise ValueError("Файл закрыт или недоступен для записи") from None

        if not (f1_writable and f2_writable):
            raise ValueError("Файл закрыт или недоступен для записи")

        self.file1.write(text)
        self.file2.write(text)

    def close(self):
        self.file1.close()
        self.file2.close()

    def writable(self):
        try:
            return self.file1.writable() and self.file2.writable()
        except ValueError:
            return False

    def closed(self):
        return self.file1.closed and self.file2.closed
