from spm.__wrapper__ import Runtime


def spm_slice2vol_reslice(*args, **kwargs):
    """
      Slice-to-volume alignment reslicing  
        FORMAT spm_slice2vol_reslice(Nii,Q,fwhm)  
         
        Nii  - NIfTI data structure encoding volumes to align  
               Most all have the same dimensions  
        Q    - A 3D array of slicewise motion parameters  
        fwhm - Smoothing FWHM (mm)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_slice2vol_reslice.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_slice2vol_reslice", *args, **kwargs, nargout=0)
