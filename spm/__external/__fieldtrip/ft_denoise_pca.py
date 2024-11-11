from spm.__wrapper__ import Runtime


def ft_denoise_pca(*args, **kwargs):
    """
      FT_DENOISE_PCA performs a principal component analysis (PCA) on specified reference  
        channels and subtracts the projection of the data of interest onto this orthogonal  
        basis from the data of interest. This is the algorithm which is applied by BTi/4D to  
        compute noise cancellation weights on a dataset of interest. This function has been  
        designed for BTi/4D MEG data, but can also be applied to data from other MEG systems.  
         
        Use as  
          [dataout] = ft_denoise_pca(cfg, data)  
        or as  
          [dataout] = ft_denoise_pca(cfg, data, refdata)  
        where "data" is a raw data structure that was obtained with FT_PREPROCESSING. If  
        you specify the additional input "refdata", the specified reference channels for  
        the regression will be taken from this second data structure. This can be useful  
        when reference-channel specific preprocessing needs to be done (e.g. low-pass  
        filtering).  
         
        The output structure dataout contains the denoised data in a format that is  
        consistent with the output of FT_PREPROCESSING.  
         
        The configuration should contain  
          cfg.refchannel = the channels used as reference signal (default = 'MEGREF')  
          cfg.channel    = the channels to be denoised (default = 'MEG')  
          cfg.truncate   = optional truncation of the singular value spectrum (default = 'no')  
          cfg.zscore     = standardise reference data prior to PCA (default = 'no')  
          cfg.pertrial   = 'no' (default) or 'yes'. Regress out the references on a per trial basis  
          cfg.trials     = list of trials that are used (default = 'all')  
          cfg.updatesens = 'no' or 'yes' (default = 'yes')  
         
        if cfg.truncate is integer n > 1, n will be the number of singular values kept.  
        if 0 < cfg.truncate < 1, the singular value spectrum will be thresholded at the  
        fraction cfg.truncate of the largest singular value.  
         
        See also FT_PREPROCESSING, FT_DENOISE_SYNTHETIC, FT_DENOISE_SSP  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_denoise_pca.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_denoise_pca", *args, **kwargs)
