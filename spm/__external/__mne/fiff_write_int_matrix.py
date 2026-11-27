from spm._runtime import Runtime


def fiff_write_int_matrix(*args, **kwargs):
    r"""
       
        fiff_write_int_matrix(fid,kind,mat)  
          
        Writes a integer matrix tag  
         
            fid           An open fif file descriptor  
            kind          The tag kind  
            mat           The data matrix  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_write_int_matrix.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_int_matrix", *args, **kwargs, nargout=0)
