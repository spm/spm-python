from spm._runtime import Runtime


def fiff_read_proj(*args, **kwargs):
    r"""
       
        [ projdata ] = fiff_read_proj(fid,node,ch_rename)  
         
        Read the SSP data under a given directory node  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_read_proj.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_read_proj", *args, **kwargs)
