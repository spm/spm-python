from spm._runtime import Runtime


def readCPersist(*args, **kwargs):
    r"""
       Version 1.2   24 April 2007   Modified to close the CPersist file if a really huge  
         taglength is encountered.  Recently discovered .acq files with the string 'ssss' added  
         at the end of the file after the final 'EndofParameters' string.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/ctf/readCPersist.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("readCPersist", *args, **kwargs)
