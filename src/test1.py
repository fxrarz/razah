import io, threading
class streamIO(io.BytesIO):
    """
    memoryStreamIO

    a in memory file like stream object 
    """

    def __init__(self):
        super().__init__()
        self._wIndex = 0
        self._rIndex = 0
        self._mutex = threading.Lock()

    def write(self, d : bytearray):
        self._mutex.acquire()
        r = super().write(d)
        self._wIndex += len(d)
        self._mutex.release()
        return r

    def read(self, n : int):
        self._mutex.acquire()
        super().seek(self._rIndex)
        r = super().read(n)
        self._rIndex += len(r)
        # now we are checking if we can
        if self._rIndex == self._wIndex:
            super().truncate(0)
            super().seek(0)
            self._rIndex = 0
            self._wIndex = 0
        self._mutex.release()
        return r

    def seek(self, n):
        self._mutex.acquire()
        self._rIndex = n
        r = super().seek(n)
        self._mutex.release()
        return r


if __name__ == '__main__':
    a = streamIO()

    a.write("hello".encode())
    txt = (a.read(100)).decode()
    print(txt)

    a.write("abc".encode())
    txt = (a.read(100)).decode()
    print(txt)

