from spm.__wrapper__ import Runtime


def mne_find_events(*args, **kwargs):
    """
       
         
          [eventlist] = mne_find_events(fname, stim_channel, consecutive, output)  
         
          Find event from raw file  
         
          fname        - string; .fiff raw data file name  
          stim_channel - int; the channel that record event  
          consecutive  - bool | 'increasing'  
                         If True, consider instances where the value of the events  
                         channel changes without first returning to zero as multiple  
                         events. If False, report only instances where the value of the  
                         events channel changes from/to zero. If 'increasing', report  
                         adjacent events only when the second event code is greater than  
                         the first.  
          output       - 'onset' | 'offset' | 'step'  
                         Whether to report when events start, when events end, or both.  
         
          eventlist    - size = (n_events, 3)  
                         The first column contains the event time in samples and the third  
                         column contains the event id. If output = 'onset' or 'step', the  
                         second column contains the value of the stim channel immediately  
                         before the event/step. For output = 'offset', the second column  
                         contains the value of the stim channel after the event offset.  
         
          Authors: Fu-Te Wong (zuxfoucault@gmail.com),  
                   Chien-Chung Chen / Visual Neuroscience Lab, National Taiwan University  
          Version 1.0 2017/9/17  
          License: BSD (3-clause)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_find_events.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_find_events", *args, **kwargs)
