from spm.__wrapper__ import Runtime


def spm_slice2vol_estimate(*args, **kwargs):
    """
      Slice-to-volume alignment estimation  
        FORMAT [Q,mu] = spm_slice2vol_estimate(Nii)  
         
        Nii - NIfTI data structure encoding volumes to align  
              Must all have the same dimensions  
        Q   - A 3D array of slicewise motion parameters  
        mu  - Population average  
         
        This function has not been thoroughly evaluated yet, but it should serve  
        as a useful starting point for coding up several different applications.  
        It worked reasonably well for an fMRI time series where the subject moved  
        much more than is typical.  
         
        Some possible extensions include:  
        * Use a higher degree B-spline for pushing and pulling operations, and  
          properly consider slice profiles.  
        * Consider a TV regulariser in the template update. See:  
              Brudfors M. Generative Models for Preprocessing of Hospital Brain  
              Scans (Doctoral dissertation, UCL (University College London)).  
        * Use a more robust objective function than L2, which may better handle  
          outliers. Alternatively, use a voxel-specific variance (or attempt to  
          model more of the covariance).  
        * Consider combining with an unwarping approach to handle EPI  
          distortions. See:  
              Andersson JL, Skare S, Ashburner J. How to correct susceptibility  
              distortions in spin-echo echo-planar images: application to  
              diffusion tensor imaging. Neuroimage. 2003 Oct 1;20(2):870-88.  
        * Make it more Bayesian to better handle parameter uncertainty.  
        * More nerdy folk may want to improve on the log-Euclidean  
          regularisation.  
        * etc  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_slice2vol_estimate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_slice2vol_estimate", *args, **kwargs)
