from spm._runtime import Runtime


def ft_denoise_ssp(*args, **kwargs):
    r"""
      FT_DENOISE_SSP projects out topographies based on ambient noise on  
        Neuromag/Elekta/MEGIN systems. These topographies are estimated during maintenance  
        visits from the engineers of MEGIN. Alternatively, it computes the projectors from  
        reference data (e.g., empty room) if it is given as an additional input. For the   
        best results, make sure to preprocess the reference data the same as the data to denoise.  
         
        Use as  
          [data] = ft_denoise_ssp(cfg, data)  
        or  
          [data] = ft_denoise_ssp(cfg, data, refdata)  
        where the input data should come from FT_PREPROCESSING or  
        FT_TIMELOCKANALYSIS and the configuration should contain  
          cfg.channel    = the channels to be denoised (default = 'all')  
          cfg.trials     = 'all' or a selection given as a 1xN vector (default = 'all')  
          cfg.ssp        = 'all' or a cell array of SSP names to apply (default = 'all')  
          cfg.updatesens = 'yes' or 'no', whether to update the sensor array with the spatial projector (default = 'yes')  
         
        If refdata is specified, this data will be used for the computation of the spatial projectors, by performing a PCA   
        on-the-fly. In this situation, the configuration should also contain  
          cfg.numcomponent = number of principal components to project out of the data  
                             (default = 3)  
          cfg.refchannel   = the channels used as reference signal (default = 'MEG')  
          cfg.reftrials    = 'all' or a selection given as a 1xN vector, specifies which trials to use   
                             from the reference data (default = 'all')  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_PREPROCESSING, FT_DENOISE_AMM, FT_DENOISE_DSSP,  
        FT_DENOISE_HFC, FT_DENOISE_PCA, FT_DENOISE_PREWHITEN, FT_DENOISE_SSS,  
        FT_DENOISE_SYNTHETIC, FT_DENOISE_TSR  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/ft_denoise_ssp.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_denoise_ssp", *args, **kwargs)
