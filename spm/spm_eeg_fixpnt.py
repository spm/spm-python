from spm.__wrapper__ import Runtime


def spm_eeg_fixpnt(*args, **kwargs):
    """
      Helper function to replace pos by pnt  
        FORMAT data = spm_eeg_fixpnt(data, recurse)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_fixpnt.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_fixpnt", *args, **kwargs)
