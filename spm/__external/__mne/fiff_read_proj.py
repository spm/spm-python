from spm.__wrapper__ import Runtime


def fiff_read_proj(*args, **kwargs):
    """
       
        [ projdata ] = fiff_read_proj(fid,node,ch_rename)  
         
        Read the SSP data under a given directory node  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_read_proj.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_read_proj", *args, **kwargs)
