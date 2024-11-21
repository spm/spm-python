from spm.__wrapper__ import Runtime


def ft_preproc_rectify(*args, **kwargs):
    """
      FT_PREPROC_RECTIFY rectifies the data, i.e. converts all samples with a  
        negative value into the similar magnitude positive value  
         
        Use as  
          [dat] = ft_preproc_rectify(dat)  
        where  
          dat        data matrix (Nchans X Ntime)  
         
        If the data contains NaNs, these are ignored for the computation, but  
        retained in the output.  
         
        See also PREPROC  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/preproc/ft_preproc_rectify.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_preproc_rectify", *args, **kwargs)
