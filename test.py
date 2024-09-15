on_off = False


def verif():
    global on_off
    if on_off:
        print("True")
        on_off = False
    else:
        print("False")
        on_off = True


for i in range(5):
    verif()
