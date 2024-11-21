from spm.__wrapper__ import Runtime


def ft_timelockbaseline(*args, **kwargs):
    """
      FT_TIMELOCKBASELINE performs baseline correction for ERF and ERP data. To apply  
        baseline correction to data that is not timelocked, use ft_preprocessing instead.  
         
        Use as  
           [timelock] = ft_timelockbaseline(cfg, timelock)  
        where the timelock data is the output from FT_TIMELOCKANALYSIS, and the  
        configuration should contain  
          cfg.baseline     = [begin end] (default = 'no')  
          cfg.channel      = cell-array, see FT_CHANNELSELECTION  
          cfg.parameter    = field for which to apply baseline normalization, or  
                             cell-array of strings to specify multiple fields to normalize  
                             (default = 'avg')  
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_TIMELOCKANALYSIS, FT_FREQBASELINE, FT_TIMELOCKGRANDAVERAGE, FT_DATATYPE_TIMELOCK  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_timelockbaseline.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_timelockbaseline", *args, **kwargs)
