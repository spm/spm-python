from mpython import Runtime


def spm_preproc(*args, **kwargs):
    """
      Combined Segmentation and Spatial Normalisation

        FORMAT results = spm_preproc(V,opts)
         V    - image to work with
         opts - options
         opts.tpm      - n tissue probability images for each class
         opts.ngaus    - number of Gaussians per class (n+1 classes)
         opts.warpreg  - warping regularisation
         opts.warpco   - cutoff distance for DCT basis functions
         opts.biasreg  - regularisation for bias correction
         opts.biasfwhm - FWHM of Gaussian form for bias regularisation
         opts.regtype  - regularisation for affine part
         opts.fudge    - a fudge factor
         opts.msk      - unused
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_preproc.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_preproc", *args, **kwargs)
