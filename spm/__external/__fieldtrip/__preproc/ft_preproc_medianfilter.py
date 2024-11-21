from spm.__wrapper__ import Runtime


def ft_preproc_medianfilter(*args, **kwargs):
    """
      FT_PREPROC_MEDIANFILTER applies a median filter, which smooths the data with a  
        boxcar-like kernel, except that it keeps steps in the data. This function requires  
        the MATLAB Signal Processing toolbox.  
         
        Use as  
          [dat] = ft_preproc_medianfilter(dat, order)  
        where  
          dat        data matrix (Nchans X Ntime)  
          order      number, the length of the median filter kernel (default = 25)  
         
        If the data contains NaNs, these are ignored for the computation, but  
        retained in the output.  
         
        See also PREPROC  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/preproc/ft_preproc_medianfilter.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_preproc_medianfilter", *args, **kwargs)
