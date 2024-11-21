from spm.__wrapper__ import Runtime


def ft_preproc_detrend(*args, **kwargs):
    """
      FT_PREPROC_DETREND removes mean and linear trend from the  
        data using using a General Linear Modeling approach.  
         
        Use as  
          [dat] = ft_preproc_detrend(dat, begin, end)  
        where  
          dat        = data matrix (Nchans X Ntime)  
          begsample  = index of the begin sample for the trend estimate  
          endsample  = index of the end sample for the trend estimate  
         
        If no begin and end sample are specified for the trend estimate, it  
        will be estimated on the complete data.  
         
        See also FT_PREPROC_BASELINECORRECT, FT_PREPROC_POLYREMOVAL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/preproc/ft_preproc_detrend.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_preproc_detrend", *args, **kwargs)
