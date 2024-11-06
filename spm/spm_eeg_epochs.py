from spm.__wrapper__ import Runtime


def spm_eeg_epochs(*args, **kwargs):
    """
      Epoching continuous M/EEG data  
        FORMAT D = spm_eeg_epochs(S)  
         
        S                - input structure   
         fields of S:  
          S.D                 - MEEG object or filename of M/EEG mat-file with  
                                continuous data  
          S.bc                - baseline-correct the data [1: yes, 0: no]  
         
        Either (to use a ready-made trial definition):  
         
            S.trl             - [N x 3] trl matrix or name of the trial definition  
                                file containing 'trl' variable with such a matrix  
         
            S.conditionlabels - labels for the trials in the data  
                                [default: 'Undefined']  
         
         or  
         
            S.timewin         - time window in PST ms  
         
            S.trialdef        - structure array for trial definition with fields  
              S.trialdef.conditionlabel - string label for the condition  
              S.trialdef.eventtype      - string  
              S.trialdef.eventvalue     - string, numeric or empty  
         
         or  
                
           S.trialength       - length of arbitrary trials to split the data into  
                                (in ms). This is useful e.g. for spectral  
                                analysis of steady state data  
         
           S.conditionlabels  - labels for the trials in the data  
                                [default: 'Undefined']  
         
           S.eventpadding     - (optional) the additional time period around each  
                                trial for which the events are saved with  
                                the trial (to let the user keep and use  
                                for analysis events which are outside) {in s}  
                                [default: 0]  
         
           S.prefix           - prefix for the output file [default: 'e']  
         
         
        Output:  
        D                     - MEEG object (also written on disk)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_epochs.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_epochs", *args, **kwargs)
