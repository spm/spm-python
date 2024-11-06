from spm.__wrapper__ import Runtime


def spm_eeg_reduce(*args, **kwargs):
    """
      Apply data reduction to M/EEG dataset  
        FORMAT D = spm_eeg_reduce(S)  
        S                     - input structure  
         
        fields of S:  
          S.D                 - MEEG object or filename of M/EEG mat-file with  
            
          S.channels          - cell array of channel names. Can include generic  
                                wildcards: 'All', 'EEG', 'MEG' etc  
          S.conditions          - cell array of condition trial names.   
          S.method           - name for the spectral estimation to use. This  
                               corresponds to the name of a plug-in function that comes  
                               after 'spm_eeg_reduce_' prefix.  
          S.keeporig         - keep the original unreduced channels (1) or remove  
                               (0, default).  
          S.keepothers       - keep the other (not involved) channels  
          S.settings         - plug-in specific settings  
          S.timewin          - time windows or interest  
          S.prefix           - prefix for the output file (default - 'R')  
         
        Output:  
        D                     - M/EEG object   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_reduce.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_reduce", *args, **kwargs)
