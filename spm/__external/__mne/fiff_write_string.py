from spm.__wrapper__ import Runtime


def fiff_write_string(*args, **kwargs):
    """
       
        fiff_write_string(fid,kind,data)  
          
        Writes a string tag  
         
            fid           An open fif file descriptor  
            kind          The tag kind  
            data          The string data to write  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_write_string.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_write_string", *args, **kwargs, nargout=0)
