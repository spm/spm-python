from spm._runtime import Runtime


def spm_TVdenoise2(*args, **kwargs):
    r"""
       
        FORMAT y = spm_TVdenoise2(x, lambda, nit, y)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Spatial/spm_TVdenoise2.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_TVdenoise2", *args, **kwargs)
