from spm.__wrapper__ import Runtime


def spm_eeg_mask(*args, **kwargs):
    """
      Create a mask image for scalp-level contrasts  
        FORMAT spm_eeg_mask(S)  
         
        S         - input structure (optional)  
        (optional) fields of S:  
           image        - file name of an image containing an unsmoothed   
                          M/EEG data in voxel-space  
           timewin      - start and end of a window in peri-stimulus time [ms]  
           outfile      - output file name  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_mask.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_mask", *args, **kwargs, nargout=0)
