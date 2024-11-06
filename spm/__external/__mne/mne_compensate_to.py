from spm.__wrapper__ import Runtime


def mne_compensate_to(*args, **kwargs):
    """
       
        [newdata] = mne_compensate_to(data,to)  
         
        Apply compensation to the data as desired  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_compensate_to.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_compensate_to", *args, **kwargs)
