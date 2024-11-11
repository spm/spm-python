from spm.__wrapper__ import Runtime


def readCTFds(*args, **kwargs):
    """
      ************************************************************************  
         
          This program is provided to users of CTF MEG systems as a courtesy only.  
          It's operation has not been verified for clinical use.  
          Please do not redistribute it without permission from CTF Systems Inc.  
         
        ************************************************************************  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/ctf/readCTFds.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("readCTFds", *args, **kwargs)
