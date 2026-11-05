from spm._runtime import Runtime


def mne_fwrite3(*args, **kwargs):
    r"""
       
        mne_fwrite(fid, val)  
        write a 3 byte integer to a file  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_fwrite3.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_fwrite3", *args, **kwargs, nargout=0)
