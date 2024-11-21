from spm.__wrapper__ import Runtime


def ft_statfun_gcmi(*args, **kwargs):
    """
      FT_STATFUN_GCMI computes mutual information between the dependent variable  
        and a discrete-valued design vector.  
         
        You can specify the following configuration options:  
          cfg.preconditionflag = 0 (default), or 1, performs Gaussian copula transform  
                                 Preconditioning is computationally efficient, because for given data it needs to be done only once.  
          cfg.gcmi.method      = ['cc', 'cd_model' 'cd_mixture'], type of calculation  
          cfg.gcmi.complex     = ['abs' 'real' 'imag' 'complex' 'angle' ], how to treat complex data  
          cfg.gcmi.tra         = matrix which specifies multivariate structure  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/statfun/ft_statfun_gcmi.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_statfun_gcmi", *args, **kwargs)
