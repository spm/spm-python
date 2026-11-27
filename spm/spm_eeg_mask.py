from spm._runtime import Runtime


def spm_eeg_mask(*args, **kwargs):
    r"""
      Create a mask image for scalp-level contrasts  
        FORMAT spm_eeg_mask(S)  
         
        S         - input structure (optional)  
        (optional) fields of S:  
           image        - file name of an image containing an unsmoothed   
                          M/EEG data in voxel-space  
           timewin      - start and end of a window in peri-stimulus time [ms]  
           outfile      - output file name  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_mask.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_mask", *args, **kwargs, nargout=0)
