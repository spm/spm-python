from spm.__wrapper__ import Runtime


def binocdf(*args, **kwargs):
    """
      BINOCDF binomial cumulative distribution function  
         
        Y=BINOCDF(X,N,P) returns the binomial cumulative distribution  
        function with parameters N and P at the values in X.  
         
        See also BINOPDF and STATS (Matlab statistics toolbox)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/external/stats/binocdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("binocdf", *args, **kwargs)
