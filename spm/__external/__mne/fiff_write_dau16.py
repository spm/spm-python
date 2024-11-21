from spm.__wrapper__ import Runtime


def fiff_write_dau16(*args, **kwargs):
    """
       
        fiff_write_dau16(fid, kind, data)  
         
        Writes a 16-bit integer tag to a fif file  
         
            fid           An open fif file descriptor  
            kind          Tag kind  
            data          The integers to use as data  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_write_dau16.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_write_dau16", *args, **kwargs, nargout=0)
