from spm.__wrapper__ import Runtime


def spm_boxcars(*args, **kwargs):
  """  Generate boxcar variable  
    FORMAT [x,t,xi] = spm_boxcars(T,fs,len)  
     
    T         Length of time series (secs)  
    fs        Sampling rate, (Hz)  
    len       Length of top of boxcar (secs)  
     
    x         Event stream (1-event, 0-no event) (samples)  
    t         time index (secs) eg. for plot(t,x)   
    xi        Sample numbers of events  (samples)  
     
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mixture/spm_boxcars.m)
  """

  return Runtime.call("spm_boxcars", *args, **kwargs)
