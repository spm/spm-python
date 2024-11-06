from spm.__wrapper__ import Runtime


def spm_eeg_regressors(*args, **kwargs):
    """
      Prepare regressors for GLM analysis of M/EEG data  
        FORMAT regfile = spm_eeg_regressors(S)  
         
        S                     - input structure  
         
        fields of S:  
          S.D                 - MEEG object or filename of M/EEG mat-file   
                                for which the regressors should be prepared  
         
        Output:  
        regfile              - path to mat file in which the regressors are saved  
       __________________________________________________________________________  
         
        This is a modular function for which plugins can be developed  
        implementing specific regressor creation cases  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_regressors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_regressors", *args, **kwargs)
