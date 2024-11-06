from spm.__wrapper__ import Runtime


def spm_est_smoothness(*args, **kwargs):
    """
      Estimation of smoothness based on [residual] images  
        FORMAT [FWHM,VRpv,R] = spm_est_smoothness(V,VM,[ndf])  
         
        V     - Filenames or mapped standardized residual images  
        VM    - Filename of mapped mask image  
        ndf   - A 2-vector, [n df], the original n & dof of the linear model  
         
        FWHM  - estimated FWHM in all image directions  
        VRpv  - handle of Resels per Voxel image  
        R     - vector of resel counts  
       __________________________________________________________________________  
         
        spm_est_smoothness returns a spatial smoothness estimator based on the  
        variances of the normalized spatial derivatives as described in K.  
        Worsley, (1996). Inputs are a mask image and a number of standardized  
        residual images, or any set of mean zero, unit variance images. Output  
        is a global estimate of the smoothness expressed as the FWHM of an  
        equivalent Gaussian point spread function. An estimate of resels per  
        voxels (see spm_spm) is written as an image file ('RPV.<ext>') to the  
        current directory.  
         
        To improve the accuracy of the smoothness estimation the error degrees  
        of freedom can be supplied.  Since it is not assumed that all residual  
        images are passed to this function, the full, original sample size n  
        must be supplied as well.  
         
        The mask image specifies voxels, used in smoothness estimation, by  
        assigning them non-zero values. The dimensions, voxel sizes, orientation  
        of all images must be the same. The dimensions of the images can be of  
        dimensions 0, 1, 2 and 3.  
         
        Note that 1-dim images (lines) must exist in the 1st dimension and  
        2-dim images (slices) in the first two dimensions. The estimated fwhm  
        for any non-existing dimension is infinity.  
       __________________________________________________________________________  
         
        Refs:  
         
        K.J. Worsley (1996). An unbiased estimator for the roughness of a  
        multivariate Gaussian random field. Technical Report, Department of  
        Mathematics and Statistics, McGill University  
         
        S.J. Kiebel, J.B. Poline, K.J. Friston, A.P. Holmes, and K.J. Worsley.  
        Robust Smoothness Estimation in Statistical Parametric Maps Using  
        Standardized Residuals from the General Linear Model. NeuroImage,  
        10:756-766, 1999.  
         
        S. Hayasaka, K. Phan, I. Liberzon, K.J. Worsley, T.E. Nichols (2004).  
        Nonstationary cluster-size inference with random field and permutation  
        methods. NeuroImage, 22:676-687, 2004.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_est_smoothness.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_est_smoothness", *args, **kwargs)
