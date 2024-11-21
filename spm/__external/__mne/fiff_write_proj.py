from spm.__wrapper__ import Runtime


def fiff_write_proj(*args, **kwargs):
    """
       
        fiff_write_proj(fid,projs,ch_rename)  
         
        Writes the projection data into a fif file  
         
            fid           An open fif file descriptor  
            projs         The compensation data to write  
            ch_rename     Short-to-long channel name mapping  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_write_proj.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_write_proj", *args, **kwargs, nargout=0)
