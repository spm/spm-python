from spm.__wrapper__ import Runtime


def ft_removetemplateartifact(*args, **kwargs):
    """
      FT_REMOVETEMPLATEARTIFACT removes an artifact from preprocessed data by template  
        subtraction. The template can for example be formed by averaging an ECG-triggered  
        MEG timecourse.  
         
        Use as  
          dataclean = ft_removetemplateartifact(cfg, data, template)  
        where data is raw data as obtained from FT_PREPROCESSING and template is a averaged  
        timelock structure as obtained from FT_TIMELOCKANALYSIS. The configuration should  
        be according to  
         
          cfg.channel  = Nx1 cell-array with selection of channels (default = 'all'), see FT_CHANNELSELECTION for details  
          cfg.artifact = Mx2 matrix with sample numbers of the artifact segments, e.g. obtained from FT_ARTIFACT_EOG  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_ARTIFACT_ECG, FT_PREPROCESSING, FT_TIMELOCKANALYSIS, FT_REJECTCOMPONENT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_removetemplateartifact.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_removetemplateartifact", *args, **kwargs)
