from spm.__wrapper__ import Runtime


def spm_eeg_history(*args, **kwargs):
    """
      Generate a MATLAB script from the history of an M/EEG SPM data file  
        FORMAT H = spm_eeg_history(S)  
         
        S  - filename or input struct (optional)  
        (optional) fields of S:  
        history         - history of M/EEG object (D.history)  
        sname           - filename of the MATLAB script to generate  
         
        H               - cell array summary of history for review purposes  
       __________________________________________________________________________  
         
        In SPM for M/EEG, each preprocessing step enters its call and input  
        arguments into an internal history. The sequence of function calls that  
        led to a given file can be read by the history method (i.e. call  
        'D.history'). From this history this function generates a script (m-file)  
        which can be run without user interaction and will repeat, if run, the  
        exact sequence on the preprocessing steps stored in the history. Of  
        course, the generated script can also be used as a template for a  
        slightly different analysis or for different subjects.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_history.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_history", *args, **kwargs)
