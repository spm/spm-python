from spm._runtime import Runtime


def end2end_restingfMRI(*args, **kwargs):
    r"""
      End-to-end test for resting dataset  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/tests/end2end_restingfMRI.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("end2end_restingfMRI", *args, **kwargs)
