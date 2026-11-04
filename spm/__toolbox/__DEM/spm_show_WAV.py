from spm._runtime import Runtime


def spm_show_WAV(*args, **kwargs):
    r"""
      Graphical illustration of active inference  
        FORMAT spm_show_MDP(MDP,WAV)  
        MDP   - Hierarchical (RG) generative model (inverted)  
        WAV   - Structure for mapping discrete outcomes to WAV pixels  
         
       --------------------------------------------------------------------------  
        This auxiliary routine plots the hierarchal outcomes (posterior  
        predictive distributions) from a deep generative model. The separation of  
        temporal scales is illustrated by showing the outcomes as a sonogram.  
         
        This version is specialised for sound files, rendering the posterior  
        predictions in alp come space as a solar gram. The image graphic is  
        equipped with a callback function that will play the corresponding sound  
        following an inverse wavelet transform.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_show_WAV.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_show_WAV", *args, **kwargs, nargout=0)
