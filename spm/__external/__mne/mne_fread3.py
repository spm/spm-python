from spm._runtime import Runtime


def mne_fread3(*args, **kwargs):
    r"""
       
        [retval] = mne_fread3(fid)  
        read a 3 byte integer out of a file  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_fread3.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_fread3", *args, **kwargs)
