from spm._runtime import Runtime


def fiff_write_name_list(*args, **kwargs):
    r"""
       
        fiff_write_name_list(fid,kind,mat)  
          
        Writes a colon-separated list of names  
         
            fid           An open fif file descriptor  
            kind          The tag kind  
            data          An array of names to create the list from  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_write_name_list.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_name_list", *args, **kwargs, nargout=0)
