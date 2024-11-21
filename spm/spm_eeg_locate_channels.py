from spm.__wrapper__ import Runtime


def spm_eeg_locate_channels(*args, **kwargs):
    """
      Locate channels and generate mask for converting M/EEG data into images  
        FORMAT [Cel, x, y] = spm_eeg_locate_channels(D, n, channels)  
         
        D               - M/EEG object  
        n               - number of voxels in each direction  
        Cind            - the indices of channels in the total channel  
                          vector  
        optimise        - scale and centre locations to use more image space  
         
        Cel             - coordinates of channels in new coordinate system  
        x, y            - x and y coordinates which support data  
         
       __________________________________________________________________________  
         
        Locates channels and generates mask for converting M/EEG data to NIfTI  
        format ('analysis at sensor level').   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_locate_channels.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_locate_channels", *args, **kwargs)
