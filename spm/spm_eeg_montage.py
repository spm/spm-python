from spm.__wrapper__ import Runtime


def spm_eeg_montage(*args, **kwargs):
    """
      Rereference EEG data to new reference channel(s)  
        FORMAT [D, montage] = spm_eeg_montage(S)  
         
        S                    - input structure  
         fields of S:  
          S.D                - MEEG object or filename of M/EEG mat-file  
          S.mode             - 'write' (default) apply montage and create a new  
                                       dataset  
                               'switch' apply online montage without writing out  
                                        the data  
                               'add'    add the montage to the set of online  
                                        montages without applying it  
                               'clear'  clear all online montages and revert to  
                                        the original state  
          S.montage          -  
            A montage is specified as a structure with the fields:  
            montage.tra      - MxN matrix  
            montage.labelnew - Mx1 cell-array: new labels  
            montage.labelorg - Nx1 cell-array: original labels  
            montage.name     - (optional) montage name when using online montage  
            or as a filename of a mat-file containing the montage structure,  
            or as the index of the online montage to use  
            or as the name of the online montage  
          S.keepothers       - keep (1) or discard (0) the channels not  
                               involved in the montage [default: 1]  
                               ignored when switching between online montages  
          S.keepsensors      - keep (1) or discard (0) the sensor representations  
          S.blocksize        - size of blocks used internally to split large  
                               continuous files [default ~20Mb]  
          S.updatehistory    - if 0 the history is not updated (use1ful for  
                               functions that use montage functionality.  
          S.prefix           - prefix for the output file (default - 'M')  
         
        NOTE:  
        montage are always defined based on the raw data on disk, i.e. discarding  
        any currently applied online montage!  
        Example: Data with 256 channels, online montage with a subset of 64  
        channels. The montage must be based on the original 256 channels, not the  
        "online" 64 ones.  
         
        Output:  
        D                    - MEEG object (also written on disk)  
        montage              - the applied montage  
       __________________________________________________________________________  
         
        spm_eeg_montage applies montage provided or specified by the user to  
        data and sensors of an MEEG file and produces a new file. It works  
        correctly when no sensors are specified or when data and sensors are  
        consistent (which is ensured by spm_eeg_prep_ui).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_montage.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_montage", *args, **kwargs)
