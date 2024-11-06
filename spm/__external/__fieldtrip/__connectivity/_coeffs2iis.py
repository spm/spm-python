from spm.__wrapper__ import Runtime


def _coeffs2iis(*args, **kwargs):
    """
      COEFFS2IIS computes the instantaneous interaction strength based on the  
        MVAR-coefficients and a noise covariance matrix. The underlying  
        assumption is that the MVAR-models have been fitted in a bivariate  
        fashion. It uses the definition according to Vinck et al. Neuroimage 2015  
        (108).  
         
        Input data:  
          A = 2x2xncmbxorder, matrix with MVAR-coefficients  
          C = 2x2xncmb      , covariance matrices of the noise  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/private/coeffs2iis.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("coeffs2iis", *args, **kwargs)
