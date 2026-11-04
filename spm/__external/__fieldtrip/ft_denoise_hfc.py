from spm._runtime import Runtime


def ft_denoise_hfc(*args, **kwargs):
    r"""
      FT_DENOISE_HFC implements harmonic field correction, which models external  
        interference on the recordings as a harmonic magnetic field. It is particulaly  
        useful for MEG data with low channel numbers, such as OPM data.  
         
        The homogenous field correction method implements Tierney et al. (2021) NIMG,  
        https://doi.org/10.1016/j.neuroimage.2021.118484.  
         
        The harmonic expansion method implements Tierney et al. (2022) NIMG,  
        https://doi.org/10.1016/j.neuroimage.2022.119338.  
         
        Use as  
          data = ft_denoise_hfc(cfg, data)  
         
        The configuration should contain  
          cfg.channel         = channels for HFC (default = 'all')  
        	cfg.order           = number, spherical harmonic order (default = 1)  
                                order = 1 is a homogenous field  
                                order = 2 includes gradients  
                                order = 3 includes quadratic terms, etc.  
          cfg.trials          = which trials do you want to denoise? (default = 'all')  
          cfg.updatesens      = 'yes' or 'no', whether to update the sensor array with the spatial projector (default = 'yes')  
          cfg.feedback        = do you want feedback (default = 'yes')  
          cfg.residualcheck   = do you want to check channel residuals (default = 'yes')  
          cfg.residualthresh  = number in pT, what level of residual signal is fine for quality assurance (default = 50)  
         
        See also FT_PREPROCESSING, FT_DENOISE_AMM, FT_DENOISE_DSSP,  
        FT_DENOISE_PCA, FT_DENOISE_PREWHITEN, FT_DENOISE_SSP, FT_DENOISE_SSS,  
        FT_DENOISE_SYNTHETIC, FT_DENOISE_TSR  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/ft_denoise_hfc.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_denoise_hfc", *args, **kwargs)
