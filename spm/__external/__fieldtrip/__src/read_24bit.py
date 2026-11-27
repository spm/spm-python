from spm._runtime import Runtime


def read_24bit(*args, **kwargs):
    r"""
      READ_24BIT read a stream of 24 bit values and converts them to doubles  
        This function is designed for Biosemi BDF files and is implemented as mex  
        file for efficiency.  
         
        Use as  
          [dat] = read_24bit(filename, offset, numwords)  
         
        See also READ_16BIT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/src/read_24bit.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_24bit", *args, **kwargs)
