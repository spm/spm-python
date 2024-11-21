from spm.__wrapper__ import Runtime


def spm_eeg_contrast(*args, **kwargs):
    """
      Compute contrasts over trials or trial types  
        FORMAT D = spm_eeg_contrast(S)  
         
        S         - optional input struct  
        fields of S:  
        D         - filename of EEG mat-file with epoched data  
        c         - contrast matrix, each row computes a contrast of the data  
        label     - cell array of labels for the contrasts, the same size as  
                    number of rows in c  
        weighted  - flag whether average should be weighted by number of  
                    replications (yes (1), no (0))  
        prefix    - prefix for the output file [default: 'w']  
         
        Output:  
        D         - EEG data struct (also written to disk)  
       __________________________________________________________________________  
         
        spm_eeg_contrast computes contrasts of data, over epochs of data. The  
        input is a single MEEG file. The argument c must have dimensions  
        Ncontrasts X Nepochs, where Ncontrasts is the number of contrasts and  
        Nepochs the number of epochs, i.e. each row of c contains one contrast  
        vector. The output is a M/EEG file with Ncontrasts epochs. The typical  
        use is to compute, for display purposes, contrasts like the difference or  
        interaction between trial types in channel space.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_contrast.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_contrast", *args, **kwargs)
