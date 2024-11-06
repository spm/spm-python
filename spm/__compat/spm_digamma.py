from spm.__wrapper__ import Runtime


def spm_digamma(*args, **kwargs):
    """
      Digamma function (logarithmic derivative of the gamma function)  
        FORMAT [y] = spm_digamma(x)  
         
        x - nonnegative, real values  
        y - gamma function evaluated at each value x  
         
                           digamma(x) = d(log(gamma(x)))/dx  
       _______________________________________________________________________  
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/compat/spm_digamma.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_digamma", *args, **kwargs)
