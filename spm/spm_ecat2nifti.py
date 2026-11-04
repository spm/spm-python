from spm._runtime import Runtime


def spm_ecat2nifti(*args, **kwargs):
    r"""
      Import ECAT 7 images from CTI PET scanners  
        FORMAT N = spm_ecat2nifti(fname,opts)  
        fname    - name of ECAT file  
        opts     - options structure  
         
        N        - NIfTI object (written in current directory)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_ecat2nifti.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ecat2nifti", *args, **kwargs)
