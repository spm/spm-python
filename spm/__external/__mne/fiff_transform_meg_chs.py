from spm.__wrapper__ import Runtime


def fiff_transform_meg_chs(*args, **kwargs):
    """
       
        [res, count] = fiff_transform_meg_chs(chs,trans)  
         
        Move to another coordinate system in MEG channel channel info  
        Count gives the number of channels transformed  
         
        NOTE: Only the coil_trans field is modified by this routine, not  
        loc which remains to reflect the original data read from the fif file  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_transform_meg_chs.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_transform_meg_chs", *args, **kwargs)
