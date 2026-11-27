from spm._runtime import Runtime


def spm_eeg_inv_spatnorm(*args, **kwargs):
    r"""
      Spatial Normalisation (using Unified Segmentation)  
        Transforms individual sMRI into MNI space and save the [inverse]   
        deformations that will be needed for computing the individual mesh  
         
        FORMAT mesh = spm_eeg_inv_spatnorm(mesh)  
          
        mesh        - input data struct   
          
        mesh        - same data struct including the inverse deformation .mat file  
                      and filename of normalised (bias corrected) sMRI  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_inv_spatnorm.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_spatnorm", *args, **kwargs)
