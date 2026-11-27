from spm._runtime import Runtime


def mne_compensate_to(*args, **kwargs):
    r"""
       
        [newdata] = mne_compensate_to(data,to)  
         
        Apply compensation to the data as desired  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_compensate_to.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_compensate_to", *args, **kwargs)
