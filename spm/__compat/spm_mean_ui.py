from spm._runtime import Runtime


def spm_mean_ui(*args, **kwargs):
    r"""
      Prompt for a series of images and averages them  
       __________________________________________________________________________  
         
        This function is deprecated. Use spm_mean instead.  
       __________________________________________________________________________  
        Copyright (C) 1998-2011 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/compat/spm_mean_ui.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mean_ui", *args, **kwargs, nargout=0)
