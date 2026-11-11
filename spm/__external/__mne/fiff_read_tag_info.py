from spm._runtime import Runtime


def fiff_read_tag_info(*args, **kwargs):
    r"""
       
        [fid,dir] = fiff_open(fname)  
         
        Open a fif file and provide the directory of tags  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_read_tag_info.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_read_tag_info", *args, **kwargs)
