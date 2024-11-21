from spm.__wrapper__ import Runtime


def mne_read_stc_file1(*args, **kwargs):
    """
       
        [stc] = mne_read_stc_file1(filename)  
          
        Reads an stc file. The returned structure has the following fields  
         
            tmin           The first time point of the data in seconds  
            tstep          Time between frames in seconds  
            vertices       vertex indices (1 based)  
            data           The data matrix (nvert * ntime)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_read_stc_file1.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_read_stc_file1", *args, **kwargs)
