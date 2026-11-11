from spm._runtime import Runtime


def writeRes4(*args, **kwargs):
    r"""
       Write the new .res4 file.  Use ieee-be (big endian) format  
         Character-string output is done using function writeCTFstring which  
         checks that strings are the correct length for the .res4 file format.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/ctf/writeRes4.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("writeRes4", *args, **kwargs)
