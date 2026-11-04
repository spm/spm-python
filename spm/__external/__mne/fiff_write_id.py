from spm._runtime import Runtime


def fiff_write_id(*args, **kwargs):
    r"""
       
        fiff_write_id(fid,kind,id)  
          
        Writes fiff id   
         
            fid           An open fif file descriptor  
            kind          The tag kind  
            id            The id to write  
         
        If the id argument is missing it will be generated here  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_write_id.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_id", *args, **kwargs, nargout=0)
