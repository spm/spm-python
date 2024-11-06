from spm.__wrapper__ import Runtime


def spm_subfun(*args, **kwargs):
    """
      Enable calling local functions  
        FORMAT [o1,o2,...] = spm_subfun(localfunctions,action,i1,i2,...)  
         
        The function is supposed to be inserted into multifunction m-files so  
        that it calls localfunctions within the scope of the m-file. The output  
        of this is used to match the action string with the name of each local  
        function to see which of them to call.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_subfun.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_subfun", *args, **kwargs)
