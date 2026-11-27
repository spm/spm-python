from spm._runtime import Runtime


def mci_plot_surface(*args, **kwargs):
    r"""
      Plot log probability surface  
        FORMAT [log_prob,S,E] = mci_plot_surface (P,M,U,Y,S,dist)  
         
        P         Parameters  
        M         Model structure  
        U         Inputs  
        Y         Data  
        S         Surface data structure  
        dist      'prior', 'like' or 'post'  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/plotting/mci_plot_surface.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_plot_surface", *args, **kwargs)
