from spm._runtime import Runtime


def binopdf(*args, **kwargs):
    r"""
      BINOPDF binomial probability density function  
         
        Y = BINOPDF(X,N,P) returns the binomial probability density  
        function with parameters N and P at the values in X.  
         
        See also BINOCDF and STATS (Matlab statistics toolbox)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/stats/binopdf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("binopdf", *args, **kwargs)
