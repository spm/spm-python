from spm._runtime import Runtime


def mne_find_channel(*args, **kwargs):
    r"""
       
        [which] = mne_find_channel(info,name)  
         
        Find a channel by name employing the info structure  
        output by mne_raw2mat or mne_epochs2mat  
         
        epoch - The data structure containing the channel information  
        name  - name of the channel to look for  
         
        Returns index of the channel in the data  
        If the channel is not found, returns -1  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_find_channel.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_find_channel", *args, **kwargs)
