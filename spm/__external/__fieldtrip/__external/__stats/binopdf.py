from spm.__wrapper__ import Runtime


def binopdf(*args, **kwargs):
    """
      BINOPDF binomial probability density function  
         
        Y = BINOPDF(X,N,P) returns the binomial probability density  
        function with parameters N and P at the values in X.  
         
        See also BINOCDF and STATS (Matlab statistics toolbox)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/external/stats/binopdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("binopdf", *args, **kwargs)
