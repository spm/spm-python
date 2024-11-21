from spm.__wrapper__ import Runtime


def mne_ex_read_epochs(*args, **kwargs):
    """
       
          Example of reading raw data  
         
          [ data, times, ch_names ] = mne_ex_read_epochs(fname,event,eventname,tmin,tmax)  
         
          Input :  
         
          fname       - The name of the input file  
          event       - The event  
          eventname   - Name of the event file  
          tmin        - Starting time in seconds  
          tmax        - Ending time in seconds  
         
          Output :  
         
          data        - Array of structures corresponding to the epochs with fields:  
         
                        epoch    the epoch, channel by channel  
                        event    event #  
                        tmin     starting time in the raw data file (initial skip omitted)  
                        tmax     ending stime in the raw data file (initial skip omitted)  
         
          times       - The time points of the samples, in seconds  
          ch_names    - Names of the channels included  
         
         
          NOTE 1: The purpose of this function is to demonstrate the raw data reading  
          routines. You may need to modify this for your purposes  
         
          NOTE 2: You need to run mne_process_raw once as  
         
          mne_process_raw --raw mne_ex_read_epochs --projoff  
         
          to create the fif-format event file (or open the file in mne_browse_raw).  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_ex_read_epochs.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_ex_read_epochs", *args, **kwargs)
