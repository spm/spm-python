from spm.__wrapper__ import Runtime


def DEM_demo_song_priors(*args, **kwargs):
    """
      Demo for a bird songs: In this example, we simulate local field potential  
        using the prediction error from the song-bird example below. We look at  
        these responses under natural stimuli and after removing the second  
        level of the hierarchy to show it is necessary for veridical perception.  
        We then repeat but omitting dynamical priors by forsaking generalised   
        coordinates  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_song_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_song_priors", *args, **kwargs, nargout=0)
