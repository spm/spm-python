from spm._runtime import Runtime


def spm_subfun(*args, **kwargs):
    r"""
      Enable calling local functions  
        FORMAT [o1,o2,...] = spm_subfun(localfunctions,action,i1,i2,...)  
         
        The function is supposed to be inserted into multifunction m-files so  
        that it calls localfunctions within the scope of the m-file. The output  
        of this is used to match the action string with the name of each local  
        function to see which of them to call.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_subfun.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_subfun", *args, **kwargs)
