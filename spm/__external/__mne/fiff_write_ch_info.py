from spm.__wrapper__ import Runtime


def fiff_write_ch_info(*args, **kwargs):
    """
       
        fiff_write_ch_info(fid,ch)  
         
        Writes a channel information record to a fif file  
         
            fid           An open fif file descriptor  
            ch            The channel information structure to write  
         
            The type, cal, unit, and pos members are explained in Table 9.5  
            of the MNE manual  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_write_ch_info.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_write_ch_info", *args, **kwargs, nargout=0)
