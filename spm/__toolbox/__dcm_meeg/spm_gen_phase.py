from spm._runtime import Runtime


def spm_gen_phase(*args, **kwargs):
    r"""
      Generate state activities for trial-specific phase-coupled activity  
        FORMAT [x] = spm_gen_phase(P,M,U)  
         
        P - parameters  
        M - model structure  
        U - trial-specific effects  
         
        x - states  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_meeg/spm_gen_phase.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_gen_phase", *args, **kwargs)
