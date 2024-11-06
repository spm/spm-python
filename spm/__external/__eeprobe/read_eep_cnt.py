from spm.__wrapper__ import Runtime


def read_eep_cnt(*args, **kwargs):
    """
      READ_EEP_CNT reads continuous EEG data from an EEProbe *.cnt file  
        and returns a structure containing the header and data information.  
         
        eeg = read_eep_cnt(filename, sample1, sample2)  
         
        where sample1 and sample2 are the begin and end sample of the data  
        to be read.  
         
        eeg.label    ... labels of EEG channels  
        eeg.rate     ... sampling rate  
        eeg.npnt     ... number of sample in data segment  
        eeg.nchan    ... number of channels  
        eeg.nsample    
        eeg.time     ... array [1 x npnt] of time points (ms)  
        eeg.data     ... array [nchan x npnt] containing eeg data (uV)   
        eeg.trigger  ... array [n, 4] containing trigger information  
         
        Author: Robert Oostenveld, Aalborg University, Denmark, 11 March 2003  
         
        See also READ_EEP_TRG, READ_EEP_REJ, READ_EEP_AVR  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/eeprobe/read_eep_cnt.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_eep_cnt", *args, **kwargs)
