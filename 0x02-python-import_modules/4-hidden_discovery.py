#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
  names = dir()
  for name in names:
    if not name.startswith("__"):
      print("{:s}".format(name))
