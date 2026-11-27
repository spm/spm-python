from spm._runtime import Runtime


def spm_eeg_collapse_timefreq(*args, **kwargs):
    r"""
      Compute within-peristimulus time (or frequency) averages (contrasts) of M/EEG data in voxel-space  
        FORMAT images = spm_eeg_collapse_timefreq(S)  
         
        S      - input structure   
        fields of S:  
           images  - list of file names containing M/EEG data in voxel-space  
           timewin - C x 2 matrix of start(s) and end(s) of a window in peri-stimulus   
                     time {ms} (or frequency {Hz})  
           prefix  - prefix for the averaged images  
         
        images - cellstr of saved images file names  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_collapse_timefreq.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_collapse_timefreq", *args, **kwargs)
