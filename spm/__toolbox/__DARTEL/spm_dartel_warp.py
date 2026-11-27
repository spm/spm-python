from spm._runtime import Runtime


def spm_dartel_warp(*args, **kwargs):
    r"""
      Register images to template data  
        format spm_dartel_warp(job)  
         
        The outputs are flow fields.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DARTEL/spm_dartel_warp.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dartel_warp", *args, **kwargs)
