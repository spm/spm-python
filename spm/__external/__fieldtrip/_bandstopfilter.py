from spm._runtime import Runtime


def _bandstopfilter(*args, **kwargs):
    """
      BANDSTOPFILTER filters EEG/MEG data in a specified band  
          
        Use as  
          [filt] = bandstopfilter(dat, Fsample, Fbp, N, type, dir)  
        where  
          dat        data matrix (Nchans X Ntime)  
          Fsample    sampling frequency in Hz  
          Fbp        frequency band, specified as [Fhp Flp]  
          N          optional filter order, default is 4 (but) or 25 (fir)  
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
         
        See also LOWPASSFILTER, HIGHPASSFILTER, BANDPASSFILTER  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/bandstopfilter.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bandstopfilter", *args, **kwargs)
