from spm.__wrapper__ import Runtime


def spm_eeg_convert2images(*args, **kwargs):
    """
      Convert M/EEG data to images for statistical analysis  
        FORMAT [images, outroot] = spm_eeg_convert2images(S)  
         
        S                   - input structure (optional)  
         fields of S:  
          D          - MEEG object or filename of M/EEG mat-file with  
                       epoched data  
         
          mode       - type of images to generate one of:  
                       'scalp x time'  
                       'scalp x frequency' (average over time)  
                       'scalp' (average over time and frequency)  
                       'source' (average over time and frequency)  
                       'time x frequency' (average over channels)  
                       'time' (1D average over channels, frequency)  
                       'frequency' (1D average over channels, time)  
                       'average' (average over all dimensions to get a single  
                                  number)  
         
          conditions - cell array of condition labels (default: convert all  
                       conditions)  
          timewin    - time window to retain (in PST ms)  
          freqwin    - frequency window to retain (for TF datasets)  
          channels   - cell array of channel labels, modality or 'all'.  
          optimise   - scale and centre channel locations to use more image space  
         
          prefix     - prefix for the folder containing the images (default: none)  
         
        output:  
          images     - list of generated image files or objects  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_convert2images.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_convert2images", *args, **kwargs)
