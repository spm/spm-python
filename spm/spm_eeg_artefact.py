from spm.__wrapper__ import Runtime


def spm_eeg_artefact(*args, **kwargs):
    """
      Simple artefact detection, optionally with robust averaging  
        FORMAT D = spm_eeg_artefact(S)  
         
        S                 - input structure  
         
        fields of S:  
          S.mode            'reject' [default]: reject bad channels and trials  
                            'mark': scan the data and create events marking the  
                                    artefacts  
          S.D             - MEEG object or filename of M/EEG mat-file  
          S.badchanthresh - fraction of trials (or time) with artefacts above  
                            which a channel is declared as bad [default: 0.2]  
         
          S.append        - 1 [default]: append new markings to existing ones  
                            0: overwrite existing markings  
          S.methods       - structure array with configuration parameters for  
                            artefact detection plugins  
          S.prefix        - prefix for the output file [default: 'a']  
         
        Output:  
        D                 - MEEG object (also written on disk)  
       __________________________________________________________________________  
         
        This is a modular function for which plugins can be developed to detect  
        artefacts with any algorithm.  
        The name of a plugin function should start with 'spm_eeg_artefact_'.  
        Several plugins are already implemented annd they can be used as  
        templates for new plugins:  
         
        peak2peak         - thresholds peak-to-peak amplitude  
        (spm_eeg_artefact_peak2peak)  
         
        jump              - thresholds the difference between adjacent samples  
        (spm_eeg_artefact_jump)  
         
        flat              - detects flat segments in the data  
        (spm_eeg_artefact_flat)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_artefact.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_artefact", *args, **kwargs)
