"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    line1len = len(line1)
    line2len = len(line2)
    if(line1len < line2len):
        for index in range(0, line1len):
            if(line1[index] != line2[index]):
                return index
        return line1len
               
    elif(line1len > line2len):
        for index in range(0, line2len):
            if(line1[index] != line2[index]):
                return index
        return line2len
    
    else:
        for index in range(0, line1len):
            if(line1[index] != line2[index]):
                return index
            
    return IDENTICAL


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    
    if(len(line1.splitlines()) <= 1 and len(line2.splitlines()) <= 1):
        if(idx >= 0 and idx <= min(len(line1), len(line2))):
            return(line1+"\n"+"="*idx+"^"+"\n"+line2+"\n")
        
    return ""


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    lines1len = len(lines1)
    lines2len = len(lines2)
    if(lines1len < lines2len):
        for index in  range(0, lines1len):
            idx = singleline_diff(lines1[index], lines2[index])
            if(idx != IDENTICAL):
                return(index, idx)
        return(lines1len, 0)
                       
    elif(lines1len > lines2len):
        for index in  range(0, lines2len):
            idx = singleline_diff(lines1[index], lines2[index])
            if(idx != IDENTICAL):
                return(index, idx)
        return(lines2len, 0)
                    
    else:
        for index in range(0, lines1len):
            idx = singleline_diff(lines1[index], lines2[index])
            if(idx != IDENTICAL):
                return(index, idx)
        
    return (IDENTICAL, IDENTICAL)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    fileobj = open(filename, 'rt')
    linelist = []
    for line in fileobj:
        flag = 0
        if(('\n' in line) or ('\r' in line)):
            line1 = line.replace('\n', '').replace('\r', '')
            linelist.append(line1)
            flag = 1
        if (flag == 0):
            linelist.append(line)
    fileobj.close()        
    
    return linelist


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    tup = multiline_diff(lines1, lines2)
    tup0 = tup[0]
    tup1 = tup[1]
    if(tup != (IDENTICAL, IDENTICAL)):
        empty = ''
        if(tup[0] == len(lines1) and tup[1] == 0):
            return("Line {}:".format(tup0)+'\n'+singleline_diff_format(empty, lines2[tup0], tup1))
        elif(tup[0] == len(lines2) and tup[1] == 0):
            return("Line {}:".format(tup0)+'\n'+singleline_diff_format(lines1[tup0], empty, tup1))
        else:
            return("Line {}:".format(tup0)+'\n'+singleline_diff_format(lines1[tup0], lines2[tup0], tup1))     
    else:
        return("No differences\n")






  




