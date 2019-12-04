#! /usr/bin/env python
import yaml
import sys

with open(sys.argv[1]) as f:
    try:
        yaml.safe_load(f)
    except:
        print("invalid")
