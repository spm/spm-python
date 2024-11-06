from spm.__wrapper__ import Runtime


def spm_eeg_fix_ctf_headloc(*args, **kwargs):
    """
      Fix head localization data in a continuous CTF dataset with continuous  
        head localization. The tracking has to be valid at least some of the time  
         
        The functionality requires the original CTF header (read with CTF toolbox)  
        to be present (set S.saveorigheader = 1 at conversion).  
         
        FORMAT D = spm_eeg_fix_ctf_headloc(S)  
         
        S         - struct (optional)  
        (optional) fields of S:  
        S.D - meeg object or filename  
         
         
        Output:  
        D         - MEEG data struct or cell array of MEEG objects with the  
                    rejected trials set to bad and sensors corrected (if  
                    requested).  
         
        Disclaimer: this code is provided as an example and is not guaranteed to work  
        with data on which it was not tested. If it does not work for you, feel  
        free to improve it and contribute your improvements to the MEEGtools toolbox  
        in SPM (http://www.fil.ion.ucl.ac.uk/spm)  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_fix_ctf_headloc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_fix_ctf_headloc", *args, **kwargs)
