#!/usr/bin/python
import sys

def main():
    ofile = open("pic.ppm", "w+")
    output = "P3\n500 500\n255\n"
    r = 255
    g = 0
    b = 255
    ofile.write(output)
    for x in range(500):
        r = (r + 3) % 256
        g = (g - 1) % 256
        b = (b - 1) % 256
        rt, gt, bt = r, g, b
        output = ""
        for y in range(500):
            rt = (rt - 1) % 256
            gt = (gt + 1) % 256
            bt = (bt - 1) % 256
            output += str(rt) + " " + str(gt) + " " + str(bt) + " "
        output += "\n"
        ofile.write(output)
    ofile.close()
    print("done")

main()
