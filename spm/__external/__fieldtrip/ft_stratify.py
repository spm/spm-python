from spm.__wrapper__ import Runtime


def ft_stratify(*args, **kwargs):
    """
      FT_STRATIFY tries to reduce the variance in a specific feature in the data  
        that is not related to an effect in two or multiple conditions, but where  
        that feature may confound the analysis. Stratification is implemented by  
        randomly removing elements from the data, making the distribution of the  
        data equal on that feature.  
         
        Use as  
          [output]          = ft_stratify(cfg, input1, input2, ...), or  
          [output, binaxis] = ft_stratify(cfg, input1, input2, ...)  
         
        For the histogram and the split method, each input is a Nchan X Nobs  
        matrix. The output is a cell-array with in each cell the same data as in  
        the corresponding input, except that the observations that should be  
        removed are marked with a NaN.  
         
        For the equatespike method, each input is a Ntrials X 1 cell-array. Each  
        trial should contain the spike firing moments (i.e. a logical Nchans X  
        Nsamples matrix). The output is a cell-array with in each cell the same  
        data as in the corresponding input, except that spike numbers have been  
        equated in each trial and channel.  
         
        The configuration should contain  
          cfg.method      = 'histogram'  
                            'splithilo'  
                            'splitlohi'  
                            'splitlolo'  
                            'splithihi'  
                            'equatespike'  
         
        The following options apply only to histogram and split methods.  
          cfg.equalbinavg = 'yes'  
          cfg.numbin      = 10  
          cfg.numiter     = 2000  
         
        The following options apply only to the equatespike method.  
          cfg.pairtrials  = 'spikesort', 'linkage' or 'no' (default = 'spikesort')  
          cfg.channel     = 'all' or list with indices ( default = 'all')  
         
        See also FT_FREQSTATISTICS, FT_TIMELOCKSTATISTICS, FT_SOURCESTATISTICS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_stratify.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_stratify", *args, **kwargs)
