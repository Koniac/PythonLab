#!/usr/bin/env.python


import sys


def usage():
    print >> sys.stderr, "Usage: python %s <filename>" % (sys.argv[0])


def main():
    pass
    print "Program arguments are:", sys.argv
    print "Number of arguments is:", len(sys.argv)
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    try:
        fp = open(sys.argv[1], "r")
    except IOError, e:
        print >> sys.stderr, "Argument is not a valid filename."
        usage()
        sys.exit(1)
    x = list(fp)
    mx = 0
    mn = 11
    mxstring = ""
    mnstring = ""
    for idx, line in enumerate(x):
        tempL = line.split("    ")
        nota = int(tempL[3])
        if nota > mx:
            mxstring = line
            mx = nota
        if nota < mn:
            mnstring = line
            mn = nota
        #print tempL
    print mxstring
    print mnstring
#    print len(x)
#    for idx, line in enumerate(x):
#        print "%d : %s" % (idx+1, line),


if __name__ == "__main__":
    sys.exit(main())
