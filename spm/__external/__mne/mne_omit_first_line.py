from spm._runtime import Runtime


def mne_omit_first_line(*args, **kwargs):
    r"""
       
        [rest] = mne_omit_first_line(str)  
         
        Omit the first line in a multi-line string (useful for handling  
        error messages)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_omit_first_line.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_omit_first_line", *args, **kwargs)
