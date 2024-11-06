from spm.__wrapper__ import Runtime


def _read_ini(*args, **kwargs):
    """
      READ_INI reads a specified element from a Windows *.ini file  
         
        Use as  
          val = read_ini(filename, element, type, number)  
        where the element is a string such as  
          NumberSlices  
          NumberPositions  
          Rows  
          Columns  
          etc.  
         
        and format specifies the datatype to be returned according to  
          %d  (integer value)  
          %f  (floating point value)  
          %s  (string)  
         
        The number argument is optional to specify how many lines of data  
        should be read, the default is 1 for strings and Inf for numbers.  
         
        The token argument is optional to specifiy a character that separates  
        the values from anything not wanted.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ini.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_ini", *args, **kwargs)
