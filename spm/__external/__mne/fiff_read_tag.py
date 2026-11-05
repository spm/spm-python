from spm._runtime import Runtime


def fiff_read_tag(*args, **kwargs):
    r"""
       
        [tag] = fiff_read_tag(fid,pos)  
         
        Read one tag from a fif file.  
        if pos is not provided, reading starts from the current file position  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_read_tag.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_read_tag", *args, **kwargs)
