from spm._runtime import Runtime


def spm_DEM_ButtonDownFcn(*args, **kwargs):
    r"""
      ButtonDownFcn to play (or save) a movie or sound on button press  
        FORMAT spm_DEM_ButtonDownFcn  
         
        Requires gcbo to have appropriate UserData; see spm_DEM_movie and  
        spm_DEM_play_song  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_DEM_ButtonDownFcn.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_DEM_ButtonDownFcn", *args, **kwargs, nargout=0)
