from spm.__wrapper__ import Runtime


def spm_eeg_inv_vbecd_gui(*args, **kwargs):
    """
      GUI function for Bayesian ECD inversion  
        - load the necessary data, if not provided  
        - fill in all the necessary bits for the VB-ECD inversion routine,  
        - launch the B_ECD routine, aka. spm_eeg_inv_vbecd  
        - displays the results.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_vbecd_gui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_vbecd_gui", *args, **kwargs)
