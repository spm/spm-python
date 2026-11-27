from spm._runtime import Runtime


def spm_voice_check(*args, **kwargs):
    r"""
      Return normalised spectral energy in acoustic range  
        FORMAT [G,Y] = spm_voice_check(Y,FS,C)  
         
        Y    - timeseries  
        FS   - sampling frequency  
        C    - standard deviation of spectral smoothing [default: 1/16 seconds]  
         
        Y    - high pass ( > 512 Hz) time series  
        G    - spectral envelope  
         
        This routine applies a high pass filter by subtracting a smoothed version  
        of the timeseries (to suppress frequencies of lesson 512 Hz). The  
        absolute value of the resulting timeseriesis then convolved with a  
        Gaussian kernel, specified by C. This returns the spectral envelope in  
        terms of the root mean square energy (normalised to a minimum of zero).  
          
        see also: spm_voice_filter.m  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_voice_check.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_voice_check", *args, **kwargs)
