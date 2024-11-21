from spm.__wrapper__ import Runtime


def spm_eeg_mask2channels(*args, **kwargs):
    """
      Make a list of channel labels based on scalp mask  
        FORMAT chanind = spm_eeg_mask2channels(D, mask)  
         
        D - M/EEG object (or filename)  
        mask - mask (numeric array, nifti object or image file name)  
               if the mask is 3D channels in all the blobs will be returned  
         
        Output:  
        chanind - indices of channels in D which correspond to blobs in the mask  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_mask2channels.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_mask2channels", *args, **kwargs)
