from spm.__wrapper__ import Runtime


def ft_denoise_prewhiten(*args, **kwargs):
    """
      FT_DENOISE_PREWHITEN applies a spatial prewhitening operation to the data using the  
        inverse noise covariance matrix. The consequence is that all channels are expressed  
        in singnal-to-noise units, causing different channel types to be comparable. This  
        ensures equal weighting in source estimation on data with different channel types.  
         
        Use as  
          dataout = ft_denoise_prewhiten(cfg, datain, noise)  
        where the datain is the original data from FT_PREPROCESSING and  
        noise should contain the estimated noise covariance from  
        FT_TIMELOCKANALYSIS.  
         
        The configuration structure can contain  
          cfg.channel     = cell-array, see FT_CHANNELSELECTION (default = 'all')  
          cfg.split       = cell-array of channel types between which covariance is split, it can also be 'all' or 'no'  
          cfg.lambda      = scalar, or string, regularization parameter for the inverse  
          cfg.kappa       = scalar, truncation parameter for the inverse  
         
        The channel selection relates to the channels that are pre-whitened using the same  
        selection of channels in the noise covariance. All channels present in the input  
        data structure will be present in the output, including trigger and other auxiliary  
        channels.  
         
        See also FT_DENOISE_SYNTHETIC, FT_DENOISE_PCA, FT_DENOISE_DSSP, FT_DENOISE_TSP  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_denoise_prewhiten.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_denoise_prewhiten", *args, **kwargs)
