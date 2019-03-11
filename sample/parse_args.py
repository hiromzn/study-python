#! python3

import argparse

#
# parse arguments
#
parser = argparse.ArgumentParser(description="calculate X to the power of Y")

# exclusive options
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")

# option with value
parser.add_argument("-z", type=int, default=1, help="(x**y) * z")

# arguments
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")

# parse !
args = parser.parse_args()

#
# main program
#

# get answer
answer = ( args.x ** args.y ) * args.z

# print answer
if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} X {} equals {}".format(args.x, args.y, args.z, answer))
else:
    print("{}^{} * {} == {}".format(args.x, args.y, args.z, answer))

