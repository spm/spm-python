from spm.__wrapper__ import Runtime


def fiff_read_epochs(*args, **kwargs):
    """
       
        [epochs] = fiff_read_epochs(fname,setno)  
         
        Read epochs from file  
         
         
          Author : Martin Luessi, MGH Martinos Center  
          License : BSD 3-clause  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_read_epochs.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_read_epochs", *args, **kwargs)
