from spm.__wrapper__ import Runtime


def ft_denoise_ssp(*args, **kwargs):
    """
      FT_DENOISE_SSP projects out topographies based on ambient noise on  
        Neuromag/Elekta/MEGIN systems. These topographies are estimated during maintenance  
        visits from the engineers of MEGIN  
         
        Use as  
          [data] = ft_denoise_ssp(cfg, data)  
        where data should come from FT_PREPROCESSING and the configuration  
        should contain  
          cfg.ssp        = 'all' or a cell array of SSP names to apply (default = 'all')  
          cfg.trials     = 'all' or a selection given as a 1xN vector (default = 'all')  
          cfg.updatesens = 'no' or 'yes' (default = 'yes')  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_PREPROCESSING, FT_DENOISE_SYNTHETIC, FT_DENOISE_PCA  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_denoise_ssp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_denoise_ssp", *args, **kwargs)
