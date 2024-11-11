from spm.__wrapper__ import Runtime


def ft_connectivityanalysis(*args, **kwargs):
    """
      FT_CONNECTIVITYANALYSIS computes various measures of connectivity between  
        MEG/EEG channels or between source-level signals.  
         
        Use as  
          stat = ft_connectivityanalysis(cfg, data)  
          stat = ft_connectivityanalysis(cfg, timelock)  
          stat = ft_connectivityanalysis(cfg, freq)  
          stat = ft_connectivityanalysis(cfg, source)  
        where the first input argument is a configuration structure (see below)  
        and the second argument is the output of FT_PREPROCESSING,  
        FT_TIMELOCKANLAYSIS, FT_FREQANALYSIS, FT_MVARANALYSIS or FT_SOURCEANALYSIS.  
         
        The different connectivity metrics are supported only for specific  
        datatypes (see below).  
         
        The configuration structure has to contain  
          cfg.method  =  string, can be  
            'amplcorr',  amplitude correlation, support for freq and source data  
            'coh',       coherence, support for freq, freqmvar and source data.  
                         For partial coherence also specify cfg.partchannel, see below.  
                         For imaginary part of coherency or coherency also specify  
                         cfg.complex, see below.  
            'csd',       cross-spectral density matrix, can also calculate partial  
                         csds - if cfg.partchannel is specified, support for freq  
                         and freqmvar data  
            'dtf',       directed transfer function, support for freq and freqmvar data  
            'granger',   granger causality, support for freq and freqmvar data  
            'pdc',       partial directed coherence, support for freq and freqmvar data  
            'plv',       phase-locking value, support for freq and freqmvar data  
            'powcorr',   power correlation, support for freq and source data  
            'powcorr_ortho', power correlation with single trial  
                         orthogonalisation, support for source data  
            'ppc'        pairwise phase consistency  
            'psi',       phaseslope index, support for freq and freqmvar data  
            'wpli',      weighted phase lag index (signed one, still have to  
                         take absolute value to get indication of strength of  
                         interaction. Note that this measure has a positive  
                         bias. Use wpli_debiased to avoid this.  
            'wpli_debiased'  debiased weighted phase lag index (estimates squared wpli)  
            'wppc'       weighted pairwise phase consistency  
            'corr'       Pearson correlation, support for timelock or raw data  
            'laggedcoherence', lagged coherence estimate  
            'plm'        phase linearity measurement  
            'mim'        multivariate interaction measure, support for freq data  
            'cancoh'     canonical coherence, support for freq data  
         
        Additional configuration options are  
          cfg.channel    = Nx1 cell-array containing a list of channels which are  
                           used for the subsequent computations. This only has an effect  
                           when the input data is univariate. See FT_CHANNELSELECTION  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_connectivityanalysis.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_connectivityanalysis", *args, **kwargs)
