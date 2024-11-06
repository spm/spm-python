from spm.__wrapper__ import Runtime


def mne_make_combined_event_file(*args, **kwargs):
    """
       
          mne_make_combined_event_file(rawname,eventname,include,all,threshold)  
         
          rawname     Name of the raw data file to scan  
          eventname   Name of the text format event file to output  
          include     Stimulus channel names to combine  
         
                      This defaults to STI 001...STI 006  
         
          all         If true, include all trigger line transitions in the file  
                      instead of the leading edges only  
          threshold   Threshold for detection of transition between inactive and active states  
         
          Create both a fif and eve format event file combining STI 001...STI 006  
          This function facilitates processing of Neuromag 122 data which do not  
          contain a composite trigger channel  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_make_combined_event_file.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_make_combined_event_file", *args, **kwargs, nargout=0)
