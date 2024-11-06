from spm.__wrapper__ import Runtime


def spm_MDP_plot(*args, **kwargs):
    """
      creates a movie of hierarchical expectations and outcomes  
        FORMAT spm_MDP_plot(MDP))  
         
        MDP - nested MDP (and DEM) structures  
            - (requires fields to specify the labels of states and outcomes)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_plot.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MDP_plot", *args, **kwargs, nargout=0)
