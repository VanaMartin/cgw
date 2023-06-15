#!/usr/bin/env python3
import click
import sys

@click.command("parse")
@click.argument("filename")
def parse(filename, vocab="Vocab.gr"):
    with open(vocab, "r") as f:
        cnt = [ _.strip() for _ in f.readlines() if not _.startswith("#") ]
        
    with open(filename, "r") as f:
        data = [ _.strip() for _ in f.readlines() if not _.startswith("#") ]

    look = {}

    for x in [ _.split() for _ in cnt if _ != "" ]:
        for _ in x[2:]:
            look[_] = x[1]

    print(look)
   
    for d in data:
        line = []
        for x in d.split():
            line.append(look[x])
        print(d)
        print(line)


if __name__ == "__main__":
    sys.exit(parse())
