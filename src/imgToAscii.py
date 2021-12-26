import ascii_magic


def PrintAscii(img):
    output = ascii_magic.from_image_file(img,columns=150,char="#")


    return ascii_magic.to_terminal(output)
