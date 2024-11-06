from spm.__wrapper__ import Runtime


def ft_statfun_diff_itc(*args, **kwargs):
    """
      FT_STATFUN_DIFF_ITC computes the difference in the inter-trial coherence between  
        two conditions. The input data for this test should consist of complex-values  
        spectral estimates, e.g. computed using FT_FREQANALYSIS with cfg.method='mtmfft',  
        'wavelet' or 'mtmconvcol'.  
         
        The ITC is a measure of phase consistency over trials. By randomlly shuffling the  
        trials  between the two consitions and repeatedly computing the ITC difference, you  
        can test the significance of the two conditions having a different ITC.  
         
        A difference in the number of trials poer condition will affect the ITC, however  
        since the number of trials remains the same for each random permutation, this bias  
        is reflected in the randomization distribution.  
         
        Use this function by calling the high-level statistic functions as  
          [stat] = ft_freqstatistics(cfg, freq1, freq2, ...)  
        with the following configuration option:  
          cfg.statistic = 'ft_statfun_diff_itc'  
         
        For this specific statistic there is no known parametric distribution, hence the  
        probability and critical value cannot be computed analytically. This specific  
        statistic can therefore only be used with cfg.method='montecarlo'. If you want to  
        do this in combination with cfg.correctm='cluster', you also need to specify  
        cfg.clusterthreshold='nonparametric_common' or 'nonparametric_individual'.  
         
        You can specify the following configuration options:  
          cfg.complex = string, 'diffabs' (default) to compute the difference of the absolute ITC values,  
                        or 'absdiff' to compute the absolute value of the difference in the complex ITC values.  
         
        The experimental design is specified as:  
          cfg.ivar  = independent variable, row number of the design that contains the labels of the conditions to be compared (default=1)  
         
        The labels for the independent variable should be specified as the number 1 and 2.  
         
        See also FT_FREQSTATISTICS and FT_STATISTICS_MONTECARLO  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/statfun/ft_statfun_diff_itc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_statfun_diff_itc", *args, **kwargs)
