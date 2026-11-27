from spm._runtime import Runtime


def spm_eeg_remove_dbs_artefact(*args, **kwargs):
    r"""
      Template-based DBS artefact removal for EEG  
        FORMAT D = spm_eeg_remove_dbs_artefact(S)  
         
        S        - optional input struct  
        (optional) fields of S:  
          S.D    - MEEG object or filename of M/EEG mat-file with epoched data  
          S.Da   - MEEG object or filename of M/EEG mat-file with artefact template  
          S.timewin - 2-element vector with start and end of baseline period [ms]  
          S.artchan - name of the channel containing artefact reference  
          S.artcond - condition name to take artefact from (if more than one)  
         
        D        - MEEG object (also saved on disk if requested)  
       __________________________________________________________________________  
        Based on Peeters et al.  
        Electrophysiologic Evidence That Directional Deep Brain Stimulation Activates  
        Distinct Neural Circuits in Patients With Parkinson Disease  
        https://doi.org/10.1016/j.neurom.2021.11.002  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/spm_eeg_remove_dbs_artefact.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_remove_dbs_artefact", *args, **kwargs)
