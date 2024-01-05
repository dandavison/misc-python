x: int


def setx(newx):
    global x
    x = newx


if __name__ == "__main__":
    setx(8)
    print(x)
