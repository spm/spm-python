from spm._runtime import Runtime


def mne_read_inverse_operator(*args, **kwargs):
    r"""
       
        [inv] = mne_read_inverse_operator(fname)  
         
        Reads the inverse operator decomposition from a fif file  
         
        fname        - The name of the file  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_read_inverse_operator.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_read_inverse_operator", *args, **kwargs)
