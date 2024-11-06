from spm.__wrapper__ import Runtime


def mne_write_w_file(*args, **kwargs):
    """
      mne_write_w_file(filename, w)  
         
         writes a binary 'w' file  
         
         filename - name of file to write to  
         w        - a structure with the following fields:  
         
        vertices - vector of vertex indices (0-based)  
        data     - vector of data values  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_write_w_file.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_write_w_file", *args, **kwargs)
