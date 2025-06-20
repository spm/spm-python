from spm._runtime import Runtime


def spm_fx_Lagrangian(*args, **kwargs):
    """
      FORMAT [f] = spm_fx_Lagrangian(P,M,U)  
         
        flow subfunction for Langrangian demo  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_fx_Lagrangian.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fx_Lagrangian", *args, **kwargs)
