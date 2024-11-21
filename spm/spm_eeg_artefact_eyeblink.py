from spm.__wrapper__ import Runtime


def spm_eeg_artefact_eyeblink(*args, **kwargs):
    """
      Detects eyeblinks in SPM continuous data file  
        S              - input structure  
        fields of S:  
           S.D         - M/EEG object  
           S.chanind   - vector of indices of channels that this plugin will look at  
           S.threshold - threshold parameter (in stdev)  
         
           Additional parameters can be defined specific for each plugin.  
         
        Output:  
        res -  
           If no input is provided the plugin returns a cfg branch for itself.  
         
           If input is provided the plugin returns a matrix of size D.nchannels x D.ntrials  
           with zeros for clean channel/trials and ones for artefacts.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_artefact_eyeblink.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_artefact_eyeblink", *args, **kwargs)
