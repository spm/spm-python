from spm._runtime import Runtime


def spm_voice_onsets(*args, **kwargs):
    r"""
      Identify intervals containing acoustic energy and post onset minima  
        FORMAT [I] = spm_voice_onsets(Y,FS,C,U)  
         
        Y    - timeseries  
        FS   - sampling frequency  
        C    - Convolution kernel [Default: 1/16 sec]  
        U    - crossing threshold [Default: 1/8  a.u]  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_voice_onsets.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_voice_onsets", *args, **kwargs)
