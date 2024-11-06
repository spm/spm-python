from spm.__wrapper__ import Runtime


def spm_eeg_lgainmat(*args, **kwargs):
    """
      Load or compute if necessary a gain matrix  
        FORMAT [L,D] = spm_eeg_lgainmat(D,Is,channels)  
        D    - Data structure  
        Is   - indices of vertices  
         
        L    - Lead-field or gain matrix L(:,Is)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_lgainmat.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_lgainmat", *args, **kwargs)
