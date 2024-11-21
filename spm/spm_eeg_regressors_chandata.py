from spm.__wrapper__ import Runtime


def spm_eeg_regressors_chandata(*args, **kwargs):
    """
      Generate regressors from channel data  
        FORMAT res = spm_eeg_regressors_chandata(S)  
        S                     - input structure  
        fields of S:  
           S.D                - M/EEG object  
         
           Additional parameters can be defined specific for each plugin  
        Output:  
         res -  
          If no input is provided the plugin returns a cfg branch for itself  
         
          If input is provided the plugin returns  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_regressors_chandata.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_regressors_chandata", *args, **kwargs)
