from spm.__wrapper__ import Runtime


def _lowpassfilter(*args, **kwargs):
    """
      LOWPASSFILTER removes high frequency components from EEG/MEG data  
          
        Use as  
          [filt] = lowpassfilter(dat, Fsample, Flp, N, type, dir)  
        where  
          dat        data matrix (Nchans X Ntime)  
          Fsample    sampling frequency in Hz  
          Flp        filter frequency  
          N          optional filter order, default is 6 (but) or 25 (fir)  
          type       optional filter type, can be  
                       'but' Butterworth IIR filter (default)  
                       'fir' FIR filter using MATLAB fir1 function   
          dir        optional filter direction, can be  
                       'onepass'         forward filter only  
                       'onepass-reverse' reverse filter only, i.e. backward in time  
                       'twopass'         zero-phase forward and reverse filter (default)  
         
        Note that a one- or two-pass filter has consequences for the  
        strength of the filter, i.e. a two-pass filter with the same filter  
        order will attenuate the signal twice as strong.  
         
        See also HIGHPASSFILTER, BANDPASSFILTER  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/lowpassfilter.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("lowpassfilter", *args, **kwargs)
