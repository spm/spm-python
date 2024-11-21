from spm.__wrapper__ import Runtime


def spm_cost_SHC_path(*args, **kwargs):
    """
      plots path for cost_SHC demo's  
        FORMAT spm_cost_SHC_path(qU,A)  
         
        qU  - DEM condotioal esimates of states  
        A.x - locations of attrcuor  
        A.d - radius  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_cost_SHC_path.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cost_SHC_path", *args, **kwargs, nargout=0)
