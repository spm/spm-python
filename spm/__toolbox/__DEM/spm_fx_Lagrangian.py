from spm._runtime import Runtime


def spm_fx_Lagrangian(*args, **kwargs):
    r"""
      FORMAT [f] = spm_fx_Lagrangian(P,M,U)  
         
        flow subfunction for Langrangian demo  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_fx_Lagrangian.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fx_Lagrangian", *args, **kwargs)
