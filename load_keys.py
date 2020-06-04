#!/usr/bin/env python

import sys
import string
from collections import defaultdict

def read_table(filename, options):
    """
      Reads keys and desired hash values pairs from a file. If no column for 
      the hash value is specified, a sequence of hash values is generated,
      from 1 to N, where N is the number of rows found in the file.
      Return a list of tuples of (key, hashval).
    """
    print("Reading table from file `%s' to extrack keys." % filename)
    try:
        fin = open(filename)
    except IOError:
        sys.exit("Error: Could not open `%s' for reading." % filename)

    keys_hashes = []
    hashval = 0

    for n, line in enumerate(fin):
        line = line.strip()
        if not line or line.startswith(options.comment):
            continue
        row = [col.strip() for col in line.split(options.splitby)]

        try:
            key = row[options.keycol - 1]
        except IndexError:
            sys.exit("%s:%i: Error: Cannot read key, not enough columns. " %
                     (filename, n+1))
        if options.hashcol:
            try:
                val = row[options.hashcol - 1]
            except IndexError:
                sys.exit("%s:%i: Error: Cannot read hash value, nott enough columns. " % (filename, n+1))
            try:
                hashval = int(val)
            except ValueError:
                sys.exit("%s:%i: Error Cannot convert `%s' to int." %
                         (filename, n+1, row[options.hashcol-1]))
        else:
            hashval += 1
        keys_hashes.append((key, hashval))
            
    fin.close()
    if not keys_hashes:
        exit("Error: no keys found in file `%s'." % filename)
    return keys_hashes

