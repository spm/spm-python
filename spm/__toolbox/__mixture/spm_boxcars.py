from spm._runtime import Runtime


def spm_boxcars(*args, **kwargs):
    r"""
      Generate boxcar variable  
        FORMAT [x,t,xi] = spm_boxcars(T,fs,len)  
         
        T         Length of time series (secs)  
        fs        Sampling rate, (Hz)  
        len       Length of top of boxcar (secs)  
         
        x         Event stream (1-event, 0-no event) (samples)  
        t         time index (secs) eg. for plot(t,x)   
        xi        Sample numbers of events  (samples)  
         
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mixture/spm_boxcars.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_boxcars", *args, **kwargs)
