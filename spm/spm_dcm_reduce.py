from spm._runtime import Runtime


def spm_dcm_reduce(*args, **kwargs):
    r"""
      Reduce the posterior of DCM given new priors (rE,rC)  
        FORMAT RCM = spm_dcm_reduce(DCM,rE,rC)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_dcm_reduce.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_reduce", *args, **kwargs)
