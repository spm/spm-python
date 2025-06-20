from spm._runtime import Runtime


def ft_denoise_sss(*args, **kwargs):
    """
      FT_DENOISE_SSS implements an spherical harmonics based  
        projection algorithm to suppress interference outside an sphere  
        spanned by an MEG array. It is based on: REFERENCE.  
         
        Use as  
          dataout = ft_denoise_sss(cfg, datain)  
        where cfg is a configuration structure that contains  
          cfg.channel          = Nx1 cell-array with selection of channels (default = 'all'), see FT_CHANNELSELECTION for details  
          cfg.trials           = 'all' or a selection given as a 1xN vector (default = 'all')  
          cfg.pertrial         = 'no', or 'yes', compute the temporal projection per trial (default = 'no')  
          cfg.demean           = 'yes', or 'no', demean the data per epoch (default = 'yes')  
          cfg.updatesens       = 'yes', or 'no', update the sensor array with the spatial projector  
          cfg.sss              = structure with parameters that determine the behavior of the algorithm  
          cfg.sss.order_in     = scalar. Order of the spherical harmonics basis that spans the in space (default = 8)   
          cfg.sss.order_out    = scalar. Order of the spherical harmonics basis that spans the out space (default = 3)   
         
        The implementation is based on Tim Tierney's code written for spm  
         
        See also FT_DENOISE_PCA, FT_DENOISE_SYNTHETIC, FT_DENOISE_TSR, FT_DENOISE_DSSP, FT_DENOISE_HFC  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_denoise_sss.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_denoise_sss", *args, **kwargs)
