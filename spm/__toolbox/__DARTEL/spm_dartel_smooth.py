from spm._runtime import Runtime


def spm_dartel_smooth(*args, **kwargs):
    r"""
      Smooth tissue probability maps  
        FORMAT [sig,a_new] = spm_dartel_smooth(t,lam,its,vx,a_old)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DARTEL/spm_dartel_smooth.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dartel_smooth", *args, **kwargs)
