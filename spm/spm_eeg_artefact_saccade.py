from spm.__wrapper__ import Runtime


def spm_eeg_artefact_saccade(*args, **kwargs):
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
         
        A simplified version of a method described by:  
        Engbert, R., & Mergenthaler, K. (2006) Microsaccades are triggered by low  
        retinal image slip. Proceedings of the National Academy of Sciences of  
        the United States of America, 103: 7192-7197.   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_artefact_saccade.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_artefact_saccade", *args, **kwargs)
