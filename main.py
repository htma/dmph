import sys
from optparse import OptionParser
from load_keys import read_table

__version__ = '0.1'
def main():
    usage = "Usage: %prog [options] KEYS_FILE"

    description = """\
    Generate  perfection hash functions from a file with keys.
    """
    parser = OptionParser(usage = usage,
                          description = description,
                          prog = sys.argv[0],
                          version = "%prog: " + __version__)

    parser.add_option("--comment",
                      action = "store",
                      default = "#",
                      help = "STR is the character, or sequence of "
                      "characters, which marks the beginning of a comment "
                      "in the input KEYS_FILE."
                      "Defalut is '%default'",
                      metavar = "STR")

    parser.add_option("--splitby",
                      action = "store",
                      default = ",",
                      help = "STR is the character by which the columns "
                      "in the input KEYS_FILE are split. "
                      "Default is '%default'",
                      metavar = "STR")

    parser.add_option("--keycol",
                      action = "store",
                      default = 1,
                      type = "int",
                      help = "Specifies the column INT in the input "
                      "KEYS_FILE which contains the keys. "
                      "Defalut is %default, i.e. the first column.",
                      metavar = "INT")

    parser.add_option("--hashcol",
                      action = "store",
                      default = 0,
                      type = "int",
                      help = "Specifies the column INT in the input "
                      "KEYS_FILE which contains the desired hash values. "
                      "By defalut the hash values are given by the sequence "
                      "1..N.",
                      metavar = "INT")

    options, args = parser.parse_args()

    if len(args) not in (1, 2):
        parser.error("incorrect number of arguments")

    keys_file = args[0]
    print("keys_file = %r" % keys_file)
    keys_hashes = read_table(keys_file, options)
    print(keys_hashes)

if __name__ == '__main__':
    main()
