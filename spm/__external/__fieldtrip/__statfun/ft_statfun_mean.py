from spm.__wrapper__ import Runtime


def ft_statfun_mean(*args, **kwargs):
    """
      FT_STATFUN_MEAN demonstrates how to compute the mean over all conditions in the  
        data. Since this does NOT depend on the experimental design, it cannot be used for  
        testing for differences between conditions.  
         
        This function serves as an example for a statfun. You can use such a function with  
        the statistical framework in FieldTrip using FT_TIMELOCKSTATISTICS,  
        FT_FREQSTATISTICS or FT_SOURCESTATISTICS to perform a statistical test, without  
        having to worry about the representation of the data.  
         
        See also FT_TIMELOCKSTATISTICS, FT_FREQSTATISTICS or FT_SOURCESTATISTICS, and see FT_STATFUN_DIFF for a similar example  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/statfun/ft_statfun_mean.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_statfun_mean", *args, **kwargs)
