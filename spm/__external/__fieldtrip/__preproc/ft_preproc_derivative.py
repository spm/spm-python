from spm.__wrapper__ import Runtime


def ft_preproc_derivative(*args, **kwargs):
    """
      FT_PREPROC_DERIVATIVE computes the temporal Nth order derivative of the  
        data  
         
        Use as  
          [dat] = ft_preproc_derivative(dat, order, deltat)  
        where  
          dat        data matrix (Nchans X Ntime)  
          order      number representing the Nth derivative (default = 1)  
          deltat     number representing the duration of 1 time step in the data  
                     (default = 1)  
         
        If the data contains NaNs, these are ignored for the computation, but  
        retained in the output.  
         
        See also PREPROC  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/preproc/ft_preproc_derivative.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_preproc_derivative", *args, **kwargs)
