from spm._runtime import Runtime


def spm_show_RGB(*args, **kwargs):
    r"""
      Graphical illustration of active inference  
        FORMAT  [J,K] = spm_show_RGB(MDP,RGB,Nt,MOVIE)  
        MDP   - Hierarchical (RG) generative model (inverted)  
        RGB   - Structure for mapping discrete outcomes to RGB pixels  
        Nt    - Number of timesteps to show images  
        MOVIE - flag for movie [default: MOVIE = 1]  
         
        [J,K] - predicted and observed RGB time-series  
         
       --------------------------------------------------------------------------  
        This auxiliary routine plots the hierarchal outcomes from a deep  
        generative model. The separation of temporal scales is illustrated by  
        showing the outcomes as a movie saved as the user data in the current  
        figure. This routine separates predicted states and paths and shows the  
        first few (predictions and observations) in pixel space.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_show_RGB.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_show_RGB", *args, **kwargs)
