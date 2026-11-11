from spm._runtime import Runtime


def spm_gen_ind(*args, **kwargs):
    r"""
      Generate a prediction of trial-specific induced activity  
        FORMAT [y] = spm_gen_ind(P,M,U)  
         
        P - parameters  
        M - neural-mass model structure  
        U - trial-specific effects  
         
        y - prediction  
         
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_meeg/spm_gen_ind.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_gen_ind", *args, **kwargs)
