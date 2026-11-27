from spm._runtime import Runtime


def _nearest_vec(*args, **kwargs):
    r"""
      locate bilateral coordinate  
        Copyright (C) 2022 Wellcome Centre for Human Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/private/nearest_vec.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("nearest_vec", *args, **kwargs)
