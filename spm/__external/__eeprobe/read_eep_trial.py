from spm.__wrapper__ import Runtime


def read_eep_trial(*args, **kwargs):
    """
       
        READ_EEP_TRIAL reads a data from an EEProbe *.cnt file  
         
        [eeg,t] = read_eep_trial(filename, triggernumber, interval);  
         
        interval = [ -2, 5] reads a window of -2 to 5 seconds around  
        the given trigger number  
         
        Script returns eeg data structure: it contains the data, labels etc  
        for the given interval  
         
        t is the time in milliseconds of the trial (at the trigger, i.e., stimulus-time)  
         
        Author: Michiel van Burik, ANT Software, Enschede, The Netherlands, 8 October 2003  
         
        See also READ_EEP_TRG, READ_EEP_REJ, READ_EEP_AVR  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/eeprobe/read_eep_trial.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_eep_trial", *args, **kwargs)
