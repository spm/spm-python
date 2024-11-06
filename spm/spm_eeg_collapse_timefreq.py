from spm.__wrapper__ import Runtime


def spm_eeg_collapse_timefreq(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_collapse_timefreq.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_collapse_timefreq", *args, **kwargs)
