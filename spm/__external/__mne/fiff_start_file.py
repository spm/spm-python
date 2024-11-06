from spm.__wrapper__ import Runtime


def fiff_start_file(*args, **kwargs):
    """
       
        [fid] = fiff_start_file(name)  
          
        Opens a fif file for writing and writes the compulsory header tags  
         
            name           The name of the file to open. It is recommended  
                           that the name ends with .fif  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_start_file.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_start_file", *args, **kwargs)
