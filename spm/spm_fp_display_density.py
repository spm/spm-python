from spm.__wrapper__ import Runtime


def spm_fp_display_density(*args, **kwargs):
    """
      Quiver plot of flow and equilibrium density  
        FORMAT [F,X] = spm_fp_display_density(M,x)  
         
        M   - model specifying flow; M(1).f;  
        x   - cell array of domain or support  
         
        F   - flow  
        X   - evaluation points  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_fp_display_density.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fp_display_density", *args, **kwargs)
