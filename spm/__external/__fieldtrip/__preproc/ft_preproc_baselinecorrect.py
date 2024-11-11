from spm.__wrapper__ import Runtime


def ft_preproc_baselinecorrect(*args, **kwargs):
    """
      FT_PREPROC_BASELINECORRECT performs a baseline correction, e.g. using the  
        prestimulus interval of the data or using the complete data  
         
        Use as  
          [dat] = ft_preproc_baselinecorrect(dat, begin, end)  
        where  
          dat        data matrix (Nchans X Ntime)  
          begsample  index of the begin sample for the baseline estimate  
          endsample  index of the end sample for the baseline estimate  
         
        If no begin and end sample are specified for the baseline estimate, it  
        will be estimated on the complete data.  
         
        If the data contains NaNs, these are ignored for the computation, but  
        retained in the output.  
         
        See also FT_PREPROC_DETREND, FT_PREPROC_POLYREMOVAL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/preproc/ft_preproc_baselinecorrect.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_preproc_baselinecorrect", *args, **kwargs)
