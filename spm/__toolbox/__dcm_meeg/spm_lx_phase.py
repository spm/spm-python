from spm._runtime import Runtime


def spm_lx_phase(*args, **kwargs):
    r"""
      Observation function for phase-coupled oscillators  
        FORMAT [G] = spm_lx_phase(P,M)  
         
        G     Observations y = Gx  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_meeg/spm_lx_phase.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_lx_phase", *args, **kwargs)
