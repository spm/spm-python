from spm.__wrapper__ import Runtime


def fiff_end_file(*args, **kwargs):
    """
       
        fiff_end_file(fid)  
         
        Writes the closing tags to a fif file and closes the file  
         
            fid           An open fif file descriptor  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_end_file.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_end_file", *args, **kwargs, nargout=0)
