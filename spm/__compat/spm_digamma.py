from spm._runtime import Runtime


def spm_digamma(*args, **kwargs):
    r"""
      Digamma function (logarithmic derivative of the gamma function)  
        FORMAT [y] = spm_digamma(x)  
         
        x - nonnegative, real values  
        y - gamma function evaluated at each value x  
         
                           digamma(x) = d(log(gamma(x)))/dx  
       _______________________________________________________________________  
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/compat/spm_digamma.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_digamma", *args, **kwargs)
