from spm.__wrapper__ import Runtime


def ft_preproc_slidingrange(*args, **kwargs):
    """
      FT_PREPROC_SLIDINGRANGE computes the range of the data in a sliding time  
        window of the width specified.  
         
        Use as  
          [dat] = ft_preproc_slidingrange(dat, width, normalize)  
        where  
          dat        data matrix (Nchans x Ntime)  
          width      width of the smoothing kernel, this should be an odd number since the window needs to be centered on an individual sample  
          normalize  boolean, whether to normalize the range of the data with the square root of the window size (default = false)  
         
        If the data contains NaNs, these are ignored for the computation, but retained in  
        the output.  
         
        See also PREPROC  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/preproc/ft_preproc_slidingrange.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_preproc_slidingrange", *args, **kwargs)
