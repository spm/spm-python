from spm._runtime import Runtime


def spm_MDP_plot(*args, **kwargs):
    r"""
      creates a movie of hierarchical expectations and outcomes  
        FORMAT spm_MDP_plot(MDP))  
         
        MDP - nested MDP (and DEM) structures  
            - (requires fields to specify the labels of states and outcomes)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_MDP_plot.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MDP_plot", *args, **kwargs, nargout=0)
