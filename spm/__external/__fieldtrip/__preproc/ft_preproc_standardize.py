from spm.__wrapper__ import Runtime


def ft_preproc_standardize(*args, **kwargs):
    """
      FT_PREPROC_STANDARDIZE performs a z-transformation or standardization  
        of the data. The standardized data will have a zero-mean and a unit  
        standard deviation.  
         
        Use as  
          [dat] = ft_preproc_standardize(dat, begsample, endsample)  
        where  
          dat        data matrix (Nchans x Ntime)  
          begsample  index of the begin sample for the mean and stdev estimate  
          endsample  index of the end sample for the mean and stdev estimate  
         
        If no begin and end sample are specified, it will be estimated on the  
        complete data.  
         
        If the data contains NaNs, these are ignored for the computation, but  
        retained in the output.  
         
        See also PREPROC  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/preproc/ft_preproc_standardize.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_preproc_standardize", *args, **kwargs)
