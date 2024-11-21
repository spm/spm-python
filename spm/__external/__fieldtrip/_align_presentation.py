from spm.__wrapper__ import Runtime


def _align_presentation(*args, **kwargs):
    """
      ALIGN_PRESENTATION is a helper function to align events from a NBS Presentation log  
        files to MEG/EEG triggers, or to a sequence of BOLD volumes.  
         
        Use as  
           events3 = align_events(event1, options1, event2, options2)  
        where  
          event1 = events from NBS Presentation log file  
          event2 = events from the MEG/EEG trigger channel  
        or  
          event1 = events from NBS Presentation log file  
          event2 = events corresponding to each volume of the BOLD sequence  
         
        The input "options1" and "options2" variables specify how the events should be  
        mapped to each other. The output "events3" variable corresponds to the events from  
        NBS Presentation log, but with the time aligned to the MEG/EEG dataset or to the  
        BOLD volumes.  
         
        See also DATA2BIDS, FT_READ_EVENT, FT_DEFINETRIAL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/align_presentation.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("align_presentation", *args, **kwargs)
