from spm.__wrapper__ import Runtime


def spm_eeg_prep(*args, **kwargs):
    """
      Prepare converted M/EEG data for further analysis  
        FORMAT D = spm_eeg_prep(S)  
        S                 - configuration structure (optional)  
        (optional) fields of S:  
          S.D             - MEEG object or filename of M/EEG mat-file  
          S.task          - action string. One of 'settype', 'defaulttype',  
                            'loadtemplate','setcoor2d', 'project3d', 'loadeegsens',  
                            'defaulteegsens', 'sens2chan', 'headshape',  
                            'coregister', 'sortconditions'  
         
          S.updatehistory - update history information [default: true]  
          S.save          - save MEEG object [default: false]  
         
        D                 - MEEG object  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_prep.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_prep", *args, **kwargs)
