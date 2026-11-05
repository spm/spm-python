from spm._runtime import Runtime


def ft_denoise_amm(*args, **kwargs):
    r"""
      FT_DENOISE_AMM implements an adaptive multipole modelling based  
        projection algorithm to suppress interference outside an ellipsoid  
        spanned by an MEG array. It is based on: REFERENCE.  
         
        Use as  
          dataout = ft_denoise_amm(cfg, datain)  
        where the input data should come from FT_PREPROCESSING or  
        FT_TIMELOCKANALYSIS and the configuration should contain  
          cfg.channel          = Nx1 cell-array with selection of channels (default = 'MEG'), see FT_CHANNELSELECTION for details  
          cfg.trials           = 'all' or a selection given as a 1xN vector (default = 'all')  
          cfg.pertrial         = 'no' or 'yes', compute the temporal projection per trial (default = 'yes')  
          cfg.demean           = 'yes' or 'no', demean the data per epoch (default = 'yes')  
          cfg.updatesens       = 'yes' or 'no', whether to update the sensor array with the spatial projector (default = 'yes')  
          cfg.amm              = structure with parameters that determine the behavior of the algorithm  
          cfg.amm.order_in     = scalar, order of the spheroidal harmonics basis that spans the in space (default = 9)  
          cfg.amm.order_out    = scalar, order of the spheroidal harmonics basis that spans the out space (default = 2)  
          cfg.amm.reducerank  
          cfg.amm.thr   
         
        The implementation is based on Tim Tierney's code written for SPM.  
         
        See also FT_PREPROCESSING, FT_DENOISE_DSSP, FT_DENOISE_HFC,  
        FT_DENOISE_PCA, FT_DENOISE_PREWHITEN, FT_DENOISE_SSP, FT_DENOISE_SSS,  
        FT_DENOISE_SYNTHETIC, FT_DENOISE_TSR  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/ft_denoise_amm.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_denoise_amm", *args, **kwargs)
