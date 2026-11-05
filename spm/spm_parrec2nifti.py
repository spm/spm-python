from spm._runtime import Runtime


def spm_parrec2nifti(*args, **kwargs):
    r"""
      Import PAR/REC images from Philips scanners into NIfTI  
        FORMAT N = spm_parrec2nifti(parfile,opts)  
        parfile   - name of PAR file  
        opts      - options structure  
           .ext     - NIfTI file extension {'img','nii'} [default: spm_file_ext]  
           .outdir  - output directory [default: pwd]  
         
        N         - NIfTI object  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_parrec2nifti.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_parrec2nifti", *args, **kwargs)
