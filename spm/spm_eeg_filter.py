from spm.__wrapper__ import Runtime


def spm_eeg_filter(*args, **kwargs):
    """
      Filter M/EEG data  
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
         
        D           - MEEG object (also written to disk)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_filter.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_filter", *args, **kwargs)
