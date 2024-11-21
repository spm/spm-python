from spm.__wrapper__ import Runtime


def spm_scope(*args, **kwargs):
    """
      Susceptibility Correction using Opposite PE  
        FORMAT vdm = spm_scope(vol1, vol2, FWHM, reg, save)  
        vol1       - path to first image (s) (same phase-encode direction)  
        vol2       - path to second image(s) (opposite phase-encode direction)  
        fwhm       - Gaussian kernel spatial scales (default: [8 4 2 1 0])  
        reg        - Regularisation settings (default: [0 10 100])  
                     See spm_field for details:  
                      - [1] Penalty on absolute values.  
                      - [2] Penalty on the `membrane energy' of the deformation.  
                        This penalises the sum of squares of the gradients of the  
                        values.  
                      - [3] Penalty on the `bending energy'. This penalises  
                         the sum of squares of the 2nd derivatives of the parameters.  
        rinterp    - Order of B-spline by which the images are sampled. A higher  
                     degree provides the better interpolation but it is slower.  
        jac        - Option to include jacobian scaling in the process to take  
                     into account the changes of intensities due to stretching  
                     and compression.  
        pref       - string to be prepended to the vdm files.  
        outdir     - output directory.  
         
       vdm        - voxel displacement map.  
         
        This is a re-implementation of the topup approach in FSL.  
         
        Reference:  
         
        J.L.R. Andersson, S. Skare, J. Ashburner. How to correct susceptibility  
        distortions in spin-echo echo-planar images: application to diffusion  
        tensor imaging. Neuroimage, 20(2):870-888, 2003.  
        https://doi.org/10.1016/s1053-8119(03)00336-7  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_scope.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_scope", *args, **kwargs)
