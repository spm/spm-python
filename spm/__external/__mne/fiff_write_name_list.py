from spm.__wrapper__ import Runtime


def fiff_write_name_list(*args, **kwargs):
    """
       
        fiff_write_name_list(fid,kind,mat)  
          
        Writes a colon-separated list of names  
         
            fid           An open fif file descriptor  
            kind          The tag kind  
            data          An array of names to create the list from  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_write_name_list.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_write_name_list", *args, **kwargs, nargout=0)
