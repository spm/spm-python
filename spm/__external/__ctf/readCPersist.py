from spm.__wrapper__ import Runtime


def readCPersist(*args, **kwargs):
    """
       Version 1.2   24 April 2007   Modified to close the CPersist file if a really huge  
         taglength is encountered.  Recently discovered .acq files with the string 'ssss' added  
         at the end of the file after the final 'EndofParameters' string.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/ctf/readCPersist.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("readCPersist", *args, **kwargs)
