from spm._runtime import Runtime


def DEM_masks_Cam(*args, **kwargs):
    r"""
      Bayesian model reduction for COVID models  
        FORMAT DEM_masks_Cam  
         
        This subroutine applies Bayesian model reduction to a DCM for COVID,  
        asking whether mask wearing can be treated as fixed parameters by  
        reducing its prior variance to 0.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_masks_Cam.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_masks_Cam", *args, **kwargs, nargout=0)
