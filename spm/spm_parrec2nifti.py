from spm.__wrapper__ import Runtime


def spm_parrec2nifti(*args, **kwargs):
    """
      Import PAR/REC images from Philips scanners into NIfTI  
        FORMAT N = spm_parrec2nifti(parfile,opts)  
        parfile   - name of PAR file  
        opts      - options structure  
           .ext     - NIfTI file extension {'img','nii'} [default: spm_file_ext]  
           .outdir  - output directory [default: pwd]  
         
        N         - NIfTI object  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_parrec2nifti.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_parrec2nifti", *args, **kwargs)
