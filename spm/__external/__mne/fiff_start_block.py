from spm._runtime import Runtime


def fiff_start_block(*args, **kwargs):
    r"""
       
        fiff_start_block(fid,kind)  
          
        Writes a FIFF_BLOCK_START tag  
         
            fid           An open fif file descriptor  
            kind          The block kind to start  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_start_block.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_start_block", *args, **kwargs, nargout=0)
