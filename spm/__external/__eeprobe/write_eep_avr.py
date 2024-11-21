from spm.__wrapper__ import Runtime


def write_eep_avr(*args, **kwargs):
    """
      WRITE_EEG_AVR writes averaged EEG data to an EEProbe *.avr file  
         
        write_eep_avr(filename, eeg)  
         
        eeg.label     ... labels of EEG channels  
        eeg.rate      ... sampling rate  
        eeg.npnt      ... number of sample in data segment  
        eeg.nchan     ... number of channels  
        eeg.nsample    
        eeg.trialc    ... total number of trials  
        eeg.nsweeps   ... averaged number of trials  
        eeg.condlab   ... condition label  
        eeg.condcol   ... condition color  
        eeg.psi       ... pre-stimulus interval(in seconds)  
        eeg.time      ... array [1 x npnt] of time points (ms)  
        eeg.data      ... array [nchan x npnt] containing eeg data (uV)   
         
        Author: Robert Smies, A.N.T. Neuro  
         
        See also READ_EEP_TRG, READ_EEP_REJ, READ_EEP_AVR  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/eeprobe/write_eep_avr.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("write_eep_avr", *args, **kwargs)
