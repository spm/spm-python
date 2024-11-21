from spm.__wrapper__ import Runtime


def mne_fread3(*args, **kwargs):
    """
       
        [retval] = mne_fread3(fid)  
        read a 3 byte integer out of a file  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_fread3.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_fread3", *args, **kwargs)
