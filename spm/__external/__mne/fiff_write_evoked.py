from spm._runtime import Runtime


def fiff_write_evoked(*args, **kwargs):
    r"""
       
        function fiff_write_evoked(name,data,datatype)  
         
        name     filename  
        data     the data structure returned from fiff_read_evoked  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_write_evoked.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_evoked", *args, **kwargs, nargout=0)
