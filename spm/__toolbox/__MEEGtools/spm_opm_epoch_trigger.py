from spm.__wrapper__ import Runtime


def spm_opm_epoch_trigger(*args, **kwargs):
    """
      Epoch M/EEG data based on supplied triggers or triggers in file;  
        FORMAT D = spm_opm_epoch_trigger(S)  
          S               - input structure  
         fields of S:  
          S.D             - SPM MEEG object                    - Default: no Default  
          S.timewin       - n x 2 matrix where n is the        - Default: replicates the first two numbers for each condition  
                            numer of conditions and the   
                            2 numbers are the time around  
                            the trigger in ms.  
          S.condLabels    - n x 1 cell containing condition    -Default: Cond N  
                            labels  
          S.bc            - boolean option to baseline         -Default: 0  
                            correct data     
          S.triggerChannels   - n x 1 cell containing trigger  - Default: all TRIG channels  
                                channel names  
        Output:  
         D           - epoched MEEG object (also written to disk)  
        trl          - the trial matrix used to epoch the data  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_opm_epoch_trigger.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_opm_epoch_trigger", *args, **kwargs)
