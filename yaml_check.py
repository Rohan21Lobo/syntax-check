#! /usr/bin/env python
import yaml
import sys

with open(sys.argv[0]) as f:
    try:
        yaml.safe_load(f)
        print("Okay")
    except:
        print("invalid")
