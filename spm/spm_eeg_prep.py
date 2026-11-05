from spm._runtime import Runtime


def spm_eeg_prep(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_prep.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_prep", *args, **kwargs)
