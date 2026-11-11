from spm._runtime import Runtime


def _coeffs2iis(*args, **kwargs):
    r"""
      COEFFS2IIS computes the instantaneous interaction strength based on the  
        MVAR-coefficients and a noise covariance matrix. The underlying  
        assumption is that the MVAR-models have been fitted in a bivariate  
        fashion. It uses the definition according to Vinck et al. Neuroimage 2015  
        (108).  
         
        Input data:  
          A = 2x2xncmbxorder, matrix with MVAR-coefficients  
          C = 2x2xncmb      , covariance matrices of the noise  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/connectivity/private/coeffs2iis.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("coeffs2iis", *args, **kwargs)
