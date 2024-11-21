from spm.__wrapper__ import Runtime


def ft_denoise_synthetic(*args, **kwargs):
    """
      FT_DENOISE_SYNTHETIC computes CTF higher-order synthetic gradients for  
        preprocessed data and for the corresponding gradiometer definition.  
         
        Use as  
          [data] = ft_denoise_synthetic(cfg, data)  
        where data should come from FT_PREPROCESSING and the configuration should contain  
          cfg.gradient = 'none', 'G1BR', 'G2BR' or 'G3BR' specifies the gradiometer  
                         type to which the data should be changed  
          cfg.trials   = 'all' or a selection given as a 1xN vector (default = 'all')  
          cfg.updatesens = 'no' or 'yes' (default = 'yes')  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_PREPROCESSING, FT_DENOISE_PCA, FT_DENOISE_SSP  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_denoise_synthetic.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_denoise_synthetic", *args, **kwargs)
