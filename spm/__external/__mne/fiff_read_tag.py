from spm.__wrapper__ import Runtime


def fiff_read_tag(*args, **kwargs):
    """
       
        [tag] = fiff_read_tag(fid,pos)  
         
        Read one tag from a fif file.  
        if pos is not provided, reading starts from the current file position  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_read_tag.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_read_tag", *args, **kwargs)
