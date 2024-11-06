from spm.__wrapper__ import Runtime


def spm_eeg_correct_sensor_data(*args, **kwargs):
    """
      Remove artefacts from the data based on their topography  
        FORMAT D = spm_eeg_correct_sensor_data(S)  
         
        S      - input structure (optional)  
        (optional) fields of S:  
          S.D    - MEEG object or filename of M/EEG mat-file  
          S.mode - 'SSP': simple projection  
                 - 'Berg': the method of Berg (see the reference below)  
        Output:  
        D      - MEEG object (also written on disk)  
         
        Implements:  
          Berg P, Scherg M.  
          A multiple source approach to the correction of eye artifacts.  
          Electroencephalogr Clin Neurophysiol. 1994 Mar;90(3):229-41.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_correct_sensor_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_correct_sensor_data", *args, **kwargs)
