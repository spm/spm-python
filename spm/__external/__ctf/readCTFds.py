from spm._runtime import Runtime


def readCTFds(*args, **kwargs):
    r"""
      ************************************************************************  
         
          This program is provided to users of CTF MEG systems as a courtesy only.  
          It's operation has not been verified for clinical use.  
          Please do not redistribute it without permission from CTF Systems Inc.  
         
        ************************************************************************  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/ctf/readCTFds.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("readCTFds", *args, **kwargs)
