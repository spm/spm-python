from spm._runtime import Runtime


def fiff_write_double_complex(*args, **kwargs):
    r"""
       
        fiff_write_double_complex(fid,kind,data)  
          
        Writes a double-precision complex tag to a fif file  
         
            fid           An open fif file descriptor  
            kind          Tag kind  
            data          The data  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_write_double_complex.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_double_complex", *args, **kwargs, nargout=0)
