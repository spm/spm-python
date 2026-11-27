from spm._runtime import Runtime


def spm_cost_SHC_path(*args, **kwargs):
    r"""
      plots path for cost_SHC demo's  
        FORMAT spm_cost_SHC_path(qU,A)  
         
        qU  - DEM condotioal esimates of states  
        A.x - locations of attrcuor  
        A.d - radius  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_cost_SHC_path.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cost_SHC_path", *args, **kwargs, nargout=0)
