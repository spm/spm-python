from spm.__wrapper__ import Runtime


def read_24bit(*args, **kwargs):
    """
      READ_24BIT read a stream of 24 bit values and converts them to doubles  
        This function is designed for Biosemi BDF files and is implemented as mex  
        file for efficiency.  
         
        Use as  
          [dat] = read_24bit(filename, offset, numwords);  
         
        See also READ_16BIT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/src/read_24bit.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_24bit", *args, **kwargs)
