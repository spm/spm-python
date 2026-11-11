from spm._runtime import Runtime


def fiff_write_epochs(*args, **kwargs):
    r"""
       
        function fiff_write_epochs(name,data)  
         
        name     filename  
        data     the data structure returned from fiff_write_evoked  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_write_epochs.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_epochs", *args, **kwargs, nargout=0)
