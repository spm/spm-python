from spm._runtime import Runtime


def spm_eeg_inv_vbecd_gui(*args, **kwargs):
    r"""
      GUI function for Bayesian ECD inversion  
        - load the necessary data, if not provided  
        - fill in all the necessary bits for the VB-ECD inversion routine,  
        - launch the B_ECD routine, aka. spm_eeg_inv_vbecd  
        - displays the results.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_inv_vbecd_gui.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_vbecd_gui", *args, **kwargs)
