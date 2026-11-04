from spm._runtime import Runtime


def fiff_finish_writing_raw(*args, **kwargs):
    r"""
       
        function fiff_finish_writing_raw(fid)  
         
        fid        of an open raw data file  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_finish_writing_raw.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_finish_writing_raw", *args, **kwargs, nargout=0)
