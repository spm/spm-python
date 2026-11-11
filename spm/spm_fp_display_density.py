from spm._runtime import Runtime


def spm_fp_display_density(*args, **kwargs):
    r"""
      Quiver plot of flow and equilibrium density  
        FORMAT [F,X] = spm_fp_display_density(M,x)  
         
        M   - model specifying flow; M(1).f;  
        x   - cell array of domain or support  
         
        F   - flow  
        X   - evaluation points  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_fp_display_density.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fp_display_density", *args, **kwargs)
