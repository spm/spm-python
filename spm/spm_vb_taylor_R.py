from spm._runtime import Runtime


def spm_vb_taylor_R(*args, **kwargs):
    r"""
      Get Taylor series approximation to posterior correlation matrices  
        FORMAT [slice] = spm_vb_taylor_R(Y,slice)  
         
        Y        - data  
        slice    - VB-GLMAR data structure  
         
        See paper VB3.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_vb_taylor_R.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_vb_taylor_R", *args, **kwargs)
