from spm._runtime import Runtime


def _notchfilter(*args, **kwargs):
    r"""
      NOTCHFILTER line noise reduction filter for EEG/MEG data  
         
        [filt] = notchfilter(dat, Fsample, Fline)  
         
        where  
          dat        data matrix (Nchans X Ntime)  
          Fsample    sampling frequency in Hz  
          Fline      line noise frequency (would normally be 50Hz)  
          N          optional filter order, default is 4  
         
        if Fline is specified as 50, a band of 48-52 is filtered out  
        if Fline is specified as [low high], that band is filtered out  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/notchfilter.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("notchfilter", *args, **kwargs)
