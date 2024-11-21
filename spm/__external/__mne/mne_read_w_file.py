from spm.__wrapper__ import Runtime


def mne_read_w_file(*args, **kwargs):
    """
       
        [w] = mne_read_w_file(filename)  
         
        Reads a binary w file into the structure w with the following fields  
         
        vertices - vector of vertex indices (0-based)  
        data     - vector of data values  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_read_w_file.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_read_w_file", *args, **kwargs)
