# From a list of files, this function reads each file and
# combines them in a single string and returns the string
def get_data(files):
    read_string = ""
    for file in files:
        with open(file, "r") as f:
            read_string += f.read()
    return(read_string)

# This function accepts multiple file arguments and prints
# the contents of each file.
def read(*files):
    print(get_data(files))

# This function accepts the first argument as the output file
# and the following arguments as files to be concatenated.
# Using this function will concatenate the passed files and
# output them to the output file. If the output file is missing,
# a new file will be created, else the existing output file will
# be overwritten.
def concat(output_file, *files):
    string_to_concat = get_data(files)
    with open(output_file, "w+") as f:
        f.write(string_to_concat)

# This function accepts the first argument as the output file
# and the following arguments as files to be appended.
# Using this function will append the passed files to the
# output file. If the output file is missing, a new file will
# be created.
def append(output_file, *files):
    string_to_append = get_data(files)
    with open(output_file, "a+") as f:
        f.write(string_to_append)

# This function creates a new file using the filename given.
# Does nothing if there is already an existing file.
def create(filename):
    open(filename, "w+")
    filename.close()