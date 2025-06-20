from spm._runtime import Runtime


def spm_eeg_select_event_ui(*args, **kwargs):
    """
      Allow the user to select an event using GUI  
        FORMAT selected = spm_eeg_select_event_ui(event)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_select_event_ui.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_select_event_ui", *args, **kwargs)
