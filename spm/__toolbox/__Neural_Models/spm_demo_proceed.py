from spm.__wrapper__ import Runtime


def spm_demo_proceed(*args, **kwargs):
    """
      prompt for OK and activate correct figure  
        FORMAT spm_demo_proceed(tag,str)  
         
        tag - graphics tag  
        str - string for dialogue box  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_demo_proceed.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_demo_proceed", *args, **kwargs, nargout=0)
