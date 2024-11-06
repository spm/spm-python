from spm.__wrapper__ import Runtime


def ft_freqbaseline(*args, **kwargs):
    """
      FT_FREQBASELINE performs baseline normalization for time-frequency data  
         
        Use as  
           [freq] = ft_freqbaseline(cfg, freq)  
        where the freq data comes from FT_FREQANALYSIS and the configuration  
        should contain  
          cfg.baseline     = [begin end] (default = 'no'), alternatively an  
                             Nfreq x 2 matrix can be specified, that provides  
                             frequency specific baseline windows.  
          cfg.baselinetype = 'absolute', 'relative', 'relchange', 'normchange', 'db', 'vssum' or 'zscore' (default = 'absolute')  
          cfg.parameter    = field for which to apply baseline normalization, or  
                             cell-array of strings to specify multiple fields to normalize  
                             (default = 'powspctrm')  
         
        See also FT_FREQANALYSIS, FT_TIMELOCKBASELINE, FT_FREQCOMPARISON,  
        FT_FREQGRANDAVERAGE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_freqbaseline.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_freqbaseline", *args, **kwargs)
