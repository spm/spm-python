from spm._runtime import Runtime


def DEM_demo_song_priors(*args, **kwargs):
    r"""
      Demo for a bird songs: In this example, we simulate local field potential  
        using the prediction error from the song-bird example below. We look at  
        these responses under natural stimuli and after removing the second  
        level of the hierarchy to show it is necessary for veridical perception.  
        We then repeat but omitting dynamical priors by forsaking generalised   
        coordinates  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_demo_song_priors.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_demo_song_priors", *args, **kwargs, nargout=0)
