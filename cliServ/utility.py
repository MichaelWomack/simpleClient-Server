__author__ = 'MichaelWomack'

# puts data into appropriate format for encoding
# it is made this way to format sys.argv if passed
def formatData(array):
    string_data = str(array[0])
    for arg in array[1:]:
        if isinstance(arg,list):
            for element in arg:
                string_data += " "
                string_data += str(element)
        else:
            string_data += " "
            string_data += str(arg)
    return string_data