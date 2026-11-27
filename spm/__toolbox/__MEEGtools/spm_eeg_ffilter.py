from spm._runtime import Runtime


def spm_eeg_ffilter(*args, **kwargs):
    r"""
      Filter M/EEG data (optimised for long datasets)  
        FORMAT D = spm_eeg_filter(S)  
         
        S           - input structure  
         Fields of S:  
          S.D       - MEEG object or filename of M/EEG mat-file  
         
          S.band    - filterband [low|high|bandpass|stop]  
          S.freq    - cutoff frequency(-ies) [Hz]  
         
         Optional fields:  
          S.type    - filter type [default: 'butterworth']  
                        'butterworth': Butterworth IIR filter  
                        'fir':         FIR filter (using MATLAB fir1 function)  
          S.order   - filter order [default: 5 for Butterworth]  
          S.dir     - filter direction [default: 'twopass']  
                        'onepass':         forward filter only  
                        'onepass-reverse': reverse filter only, i.e. backward in time  
                        'twopass':         zero-phase forward and reverse filter  
          S.prefix  - prefix for the output file [default: 'f']  
          S.chunkSize - size data segment (MB) to be filtered (default 200)  
        Currently only set up for single epoch data  
        D           - MEEG object (also written to disk)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/spm_eeg_ffilter.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_ffilter", *args, **kwargs)
