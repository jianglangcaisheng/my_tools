class MyException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


if __name__ == "__main__":
    raise Exception("My exception")
