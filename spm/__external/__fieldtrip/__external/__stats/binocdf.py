from spm._runtime import Runtime


def binocdf(*args, **kwargs):
    r"""
      BINOCDF binomial cumulative distribution function  
         
        Y=BINOCDF(X,N,P) returns the binomial cumulative distribution  
        function with parameters N and P at the values in X.  
         
        See also BINOPDF and STATS (Matlab statistics toolbox)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/stats/binocdf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("binocdf", *args, **kwargs)
