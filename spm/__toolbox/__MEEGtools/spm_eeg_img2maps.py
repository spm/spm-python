from spm._runtime import Runtime


def spm_eeg_img2maps(*args, **kwargs):
    r"""
      Make a series of scalp maps from data in an image  
        FORMAT  spm_eeg_img2maps(S)  
         
        S         - input structure (optional)  
        (optional) fields of S:  
           D              - M/EEG dataset containing the sensor locations  
           image          - file name of an image containing M/EEG data in voxel-space  
           window         - start and end of a window in peri-stimulus time [ms]  
           clim           - color limits of the plot  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/spm_eeg_img2maps.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_img2maps", *args, **kwargs, nargout=0)
