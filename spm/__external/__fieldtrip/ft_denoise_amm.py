from spm.__wrapper__ import Runtime


def ft_denoise_amm(*args, **kwargs):
    """
      FT_DENOISE_AMM implements an adaptive multipole modelling based  
        projection algorithm to suppress interference outside an ellipsoid  
        spanned by an MEG array. It is based on: REFERENCE.  
         
        Use as  
          dataout = ft_denoise_amm(cfg, datain)  
        where cfg is a configuration structure that contains  
          cfg.channel          = Nx1 cell-array with selection of channels (default = 'MEG'), see FT_CHANNELSELECTION for details  
          cfg.trials           = 'all' or a selection given as a 1xN vector (default = 'all')  
          cfg.pertrial         = 'no', or 'yes', compute the temporal projection per trial (default = 'no')  
          cfg.demean           = 'yes', or 'no', demean the data per epoch (default = 'yes')  
          cfg.updatesens       = 'yes', or 'no', update the sensor array with the spatial projector  
          cfg.amm              = structure with parameters that determine the behavior of the algorithm  
          cfg.amm.order_in     = scalar. Order of the spheroidal harmonics basis that spans the in space (default = 9)   
          cfg.amm.order_out    = scalar. Order of the spheroidal harmonics basis that spans the out space (default = 2)   
          cfg.amm.reducerank  
          cfg.amm.thr   
         
        The implementation is based on Tim Tierney's code written for spm  
         
        See also FT_DENOISE_PCA, FT_DENOISE_SYNTHETIC, FT_DENOISE_TSR, FT_DENOISE_DSSP, FT_DENOISE_HFC  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_denoise_amm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_denoise_amm", *args, **kwargs)
