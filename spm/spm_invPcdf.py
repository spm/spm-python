from spm.__wrapper__ import Runtime


def spm_invPcdf(*args, **kwargs):
    """
      Inverse Cumulative Distribution Function (CDF) of Poisson distribution  
        FORMAT x = spm_invPcdf(F,l)  
         
        F - CDF (lower tail p-value)  
        x - ordinates  
        l - Poisson mean parameter (lambda l>0) [Defaults to 1]  
       __________________________________________________________________________  
         
        spm_invPcdf returns the inverse Cumulative Distribution Function for  
        the Poisson family of distributions.  
         
        Definition:  
       --------------------------------------------------------------------------  
        The Poisson Po(l) distribution is the distribution of the number of  
        events in unit time for a stationary Poisson process with mean  
        parameter lambda=1, or equivalently rate 1/l. If random variable X is  
        the number of such events, then X~Po(l), and the CDF F(x) is  
        Pr({X<=x}.  
         
        The Poisson distribution is discrete, defined for l in [0,Inf) and x  
        in {0,1,...}, so F(x) is a discrete function. This inverse CDF  
        function returns the smallest Whole x such that the F(x) equals or  
        exceeds the given CDF probability F. I.e. F(x) is treated as a step  
        function.  
         
        Algorithm:  
       --------------------------------------------------------------------------  
        x is found by direct summation of the Poisson PDFs until F is exceeded.  
         
        References:  
       --------------------------------------------------------------------------  
        Evans M, Hastings N, Peacock B (1993)  
              "Statistical Distributions"  
               2nd Ed. Wiley, New York  
         
        Abramowitz M, Stegun IA, (1964)  
              "Handbook of Mathematical Functions"  
               US Government Printing Office  
         
        Press WH, Teukolsky SA, Vetterling AT, Flannery BP (1992)  
              "Numerical Recipes in C"  
               Cambridge  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_invPcdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_invPcdf", *args, **kwargs)
