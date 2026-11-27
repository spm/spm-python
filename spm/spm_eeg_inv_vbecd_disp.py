from spm._runtime import Runtime


def spm_eeg_inv_vbecd_disp(*args, **kwargs):
    r"""
      Display the dipoles as obtained from VB-ECD  
         
        FORMAT spm_eeg_inv_vbecd_disp('Init',D)  
        Display the latest VB-ECD solution saved in the .inv{} field of the  
        data structure D.  
         
        FORMAT spm_eeg_inv_vbecd_disp('Init',D, ind)  
        Display the ind^th .inv{} cell element, if it is actually a VB-ECD   
        solution.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_inv_vbecd_disp.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_vbecd_disp", *args, **kwargs, nargout=0)
