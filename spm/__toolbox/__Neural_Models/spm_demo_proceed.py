from spm._runtime import Runtime


def spm_demo_proceed(*args, **kwargs):
    r"""
      prompt for OK and activate correct figure  
        FORMAT spm_demo_proceed(tag,str)  
         
        tag - graphics tag  
        str - string for dialogue box  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Neural_Models/spm_demo_proceed.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_demo_proceed", *args, **kwargs, nargout=0)
