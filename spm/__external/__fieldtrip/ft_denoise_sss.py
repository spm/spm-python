from spm._runtime import Runtime


def ft_denoise_sss(*args, **kwargs):
    r"""
      FT_DENOISE_sss implements an spherical harmonics based  
        projection algorithm to suppress interference outside an sphere  
        spanned by an MEG array. It is based on: https://doi.org/10.1063/1.1935742.  
         
        Use as  
          dataout = ft_denoise_sss(cfg, datain)  
        where the input data should come from FT_PREPROCESSING or FT_TIMELOCKANALYSIS and the  
        configuration structure should contain  
          cfg.sss.origin       = 1x3 vector, specifying the origin of the spherical harmonic expansion, in coordinates and units consistent with the sensor array  
         
        other options are   
          cfg.channel          = Nx1 cell-array with selection of channels (default = 'MEG'), see FT_CHANNELSELECTION for details  
          cfg.trials           = 'all' or a selection given as a 1xN vector (default = 'all')  
          cfg.demean           = 'yes', or 'no', demean the data per epoch (default = 'yes')  
          cfg.updatesens       = 'yes', or 'no', update the sensor array with the spatial projector  
          cfg.updateheadposition = 'no', or 'yes', do movement compensation by realigning the data to a fixed head position, for CTF data only (default = 'no')  
          cfg.sss              = structure with parameters that determine the behavior of the algorithm  
          cfg.sss.order_in     = scalar, order of the spherical harmonics basis that spans the in space (default = 8)   
          cfg.sss.order_out    = scalar, order of the spherical harmonics basis that spans the out space (default = 3)   
          cfg.sss.thr          = scalar, correlation threshold for the removal of temporal components from the intersection subspace (default = 0.98)  
          cfg.sss.chunkszie    = scalar (or 'none', or 'trial'), length of segments for temporal component estimation (default = 10). If 'none', no temporal   
                                 projection will be performed. If 'trial', temporal projection (+optional headposition update) will be computed per trial   
                                 (without accounting for chunksize)   
         
        The implementation is based on Tim Tierney's code written for SPM, and with inspiration from the MNE-Python version.  
         
        See also FT_PREPROCESSING, FT_DENOISE_AMM, FT_DENOISE_DSSP,  
        FT_DENOISE_HFC, FT_DENOISE_PCA, FT_DENOISE_PREWHITEN, FT_DENOISE_SSP,  
        FT_DENOISE_SYNTHETIC, FT_DENOISE_TSR  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/ft_denoise_sss.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_denoise_sss", *args, **kwargs)
