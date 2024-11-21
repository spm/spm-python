from spm.__wrapper__ import Runtime


def spm_eeg_definetrial(*args, **kwargs):
    """
      Definition of trials based on events  
        FORMAT [trl, conditionlabels, S] = spm_eeg_definetrial(S)  
        S                 - input structure (optional)  
        (optional) fields of S:  
          S.D             - MEEG object or filename of M/EEG mat-file  
          S.timewin       - time window {in PST ms}  
          S.trialdef      - structure array for trial definition with fields (optional)  
              S.trialdef.conditionlabel - string label for the condition  
              S.trialdef.eventtype      - string  
              S.trialdef.eventvalue     - string, numeric or empty  
              S.trialdef.trlshift       - shift the triggers by a fixed amount {ms}   
                                          (e.g. projector delay).  
          S.reviewtrials  - review individual trials after selection [yes/no: 1/0]  
          S.save          - save trial definition [yes/no: 1/0]  
         
        OUTPUT:  
          trl             - Nx3 matrix [start end offset]  
          conditionlabels - Nx1 cell array of strings, label for each trial  
          S               - modified configuration structure (for history)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_definetrial.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_definetrial", *args, **kwargs)
