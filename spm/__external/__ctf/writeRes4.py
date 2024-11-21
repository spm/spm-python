from spm.__wrapper__ import Runtime


def writeRes4(*args, **kwargs):
    """
       Write the new .res4 file.  Use ieee-be (big endian) format  
         Character-string output is done using function writeCTFstring which  
         checks that strings are the correct length for the .res4 file format.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/ctf/writeRes4.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("writeRes4", *args, **kwargs)
