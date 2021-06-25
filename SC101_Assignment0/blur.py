"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    # Get the original picture size
    w = img.width
    h = img.height

    # new_img = SimpleImage.blank(w,h)
    new_img = img

    for x in range(w):
        for y in range(h):
            count = 0
            r_sum = 0
            g_sum = 0
            b_sum = 0

            for xf in range (x-1, x+2):
                for yf in range (y-1, y+2):

                    if xf >= 0 and xf < 300 and yf >=0 and yf < 300:
                        count += 1
                        r_sum = r_sum + img.get_pix(xf, yf)[0]
                        g_sum = g_sum + img.get_pix(xf, yf)[1]
                        b_sum = b_sum + img.get_pix(xf, yf)[2]

            new_img.set_pix(x, y, (int(r_sum/count),int(g_sum/count),int(b_sum/count)))
            # print(img.get_pix(x, y))
            # print(new_img.get_pix(x, y))

    return new_img

def main():
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
