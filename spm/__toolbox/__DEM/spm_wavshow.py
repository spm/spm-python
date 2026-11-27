from spm._runtime import Runtime


def spm_wavshow(*args, **kwargs):
    r"""
      rendering of a WAV sequence  
        FORMAT [s] = spm_wavshow(I,WAV)  
        I   - sonogram  
        WAV - structure  
        s   - sound  
         
        This auxiliary routine plays the sound in a time frequency matrix (I),  
        following an inverse wavelet transform. If called with no output  
        arguments, it will also plot the sonogram (time frequency representation)  
        and a sound file (timeseries) sampled from the sonogram (and sets the  
        ButtonDownFcn of the sonogram image to play the sound).  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_wavshow.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_wavshow", *args, **kwargs)
