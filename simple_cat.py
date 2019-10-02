import argparse


def get_data(files):
    """
    Return a string containing the combined content of all the files in the list parameter.

    :param files: A list of file names in the form of strings.
    :return: a string containing the combined content of all the files in the list parameter.
    """
    read_string = ""
    for file in files:
        with open(file, "r") as f:
            read_string += f.read()
    return read_string


def read(files):
    """
    Print the combined contents of all the files in the list parameter.

    :param files: A list of file names in the form of strings.
    :return: None
    """
    print(get_data(files))


def concat(output_file, files):
    """
    Concatenate all files except the last one in the list and output it to the last file in the list.

    :param output_file: Target file to output the concatenation.
    :param files: A list of file names in the form of strings.
    :return: None
    """
    string_to_concat = get_data(files)
    with open(output_file, "w+") as f:
        return f.write(string_to_concat)


def append(output_file, files):
    """
    Combine the contents of all files except the last one in the list and append it to the last file in the list.

    :param output_file: Target file to append to.
    :param files: A list of file names in the form of strings
    :return: None
    """
    string_to_append = get_data(files)
    with open(output_file, "a+") as f:
        f.write(string_to_append)


def create(filenames):
    """
    Create non-existing files in the given list parameter.

    :param filenames: A list of file names in the form of strings
    :return: None
    """
    for filename in filenames:
        f = open(filename, "w+")
        f.close()


# Adding arguments
parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="*", help="Files to be opened. Prints the contents of each file if there are no"
                                             "optional arguments.")
parser.add_argument("-a", "--append", action="store_true", help="Takes all the data from inputted files, except the "
                                                                "last and appends them to the last file. Creates a new"
                                                                " file if output file is non-existing.")
parser.add_argument("-c", "--concat", action="store_true", help="Takes all the data from inputted files, except the "
                                                                "last and concatenates them to the last file. Creates a"
                                                                " new file if output file is non-existing.")
parser.add_argument("-mk", "--make", action="store_true", help="Creates each inputted file if non-existing.")
args = parser.parse_args()
if args.append:
    append(args.files[-1], args.files[:-1])
elif args.concat:
    concat(args.files[-1], args.files[:-1])
elif args.make:
    create(args.files)
else:
    read(args.files)
