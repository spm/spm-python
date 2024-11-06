from spm.__wrapper__ import Runtime


def fiff_write_double(*args, **kwargs):
    """
       
        fiff_write_int(fid,kind,data)  
          
        Writes a double-precision floating point tag to a fif file  
         
            fid           An open fif file descriptor  
            kind          Tag kind  
            data          The data  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_write_double.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_write_double", *args, **kwargs, nargout=0)
