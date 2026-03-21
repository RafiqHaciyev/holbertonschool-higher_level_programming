#!/usr/bin/python3
print("{:s}".format(
    "".join(chr(97 + i) for i in range(26) if chr(97 + i) not in "qe")),
      end="")
