from spm.__wrapper__ import Runtime


def ft_sourcedescriptives(*args, **kwargs):
    """
      FT_SOURCEDESCRIPTIVES computes descriptive parameters of the source  
        analysis results.  
         
        Use as  
          [source] = ft_sourcedescriptives(cfg, source)  
         
        where cfg is a structure with the configuration details and source is the  
        result from a beamformer source estimation. The configuration can contain  
          cfg.cohmethod        = 'regular', 'lambda1', 'canonical'  
          cfg.powmethod        = 'regular', 'lambda1', 'trace', 'none'  
          cfg.supmethod        = 'chan_dip', 'chan', 'dip', 'none' (default)  
          cfg.projectmom       = 'yes' or 'no' (default = 'no')  
          cfg.eta              = 'yes' or 'no' (default = 'no')  
          cfg.kurtosis         = 'yes' or 'no' (default = 'no')  
          cfg.keeptrials       = 'yes' or 'no' (default = 'no')  
          cfg.keepcsd          = 'yes' or 'no' (default = 'no')  
          cfg.keepnoisecsd     = 'yes' or 'no' (default = 'no')  
          cfg.keepmom          = 'yes' or 'no' (default = 'yes')  
          cfg.keepnoisemom     = 'yes' or 'no' (default = 'yes')  
          cfg.resolutionmatrix = 'yes' or 'no' (default = 'no')  
          cfg.feedback         = 'no', 'text' (default), 'textbar', 'gui'  
         
        The following option only applies to timecourses.  
          cfg.flipori          = 'yes' or 'no' (default = 'no')  
         
        The following option only applies to single-trial timecourses.  
          cfg.fixedori         = 'within_trials' or 'over_trials' (default = 'over_trials')  
         
        If repeated trials are present that have undergone some sort of  
        resampling (i.e. jackknife, bootstrap, singletrial or rawtrial), the mean,  
        variance and standard error of mean will be computed for all source  
        parameters. This is done after applying the optional transformation  
        on the power and projected noise.  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_SOURCEANALYSIS, FT_SOURCESTATISTICS, FT_MATH  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_sourcedescriptives.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_sourcedescriptives", *args, **kwargs)
