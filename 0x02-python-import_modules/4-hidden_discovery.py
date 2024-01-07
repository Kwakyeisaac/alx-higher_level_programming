#!/usr/bin/python3
if __name__ == "__main__":
    from hidden _4 import *
    allf = dir()
    for i in range(0), len(allf)):
        if allf[i][2] != "__":
            print("{:s}".format(allf[i]))
