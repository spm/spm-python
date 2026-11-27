from spm._runtime import Runtime


def mne_read_stc_file1(*args, **kwargs):
    r"""
       
        [stc] = mne_read_stc_file1(filename)  
          
        Reads an stc file. The returned structure has the following fields  
         
            tmin           The first time point of the data in seconds  
            tstep          Time between frames in seconds  
            vertices       vertex indices (1 based)  
            data           The data matrix (nvert * ntime)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_read_stc_file1.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_read_stc_file1", *args, **kwargs)
