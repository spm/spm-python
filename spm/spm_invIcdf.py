from spm.__wrapper__ import Runtime


def spm_invIcdf(*args, **kwargs):
    """
      Inverse Cumulative Distribution Function (CDF) of Binomial distribution  
        FORMAT r = spm_invIcdf(F,n,p)  
         
        F - CDF (lower tail p-value)  
        n - Binomial n  
        p - Binomial p [Defaults to 0.5]  
        r - ordinate  
       __________________________________________________________________________  
         
        spm_invIcdf returns the inverse Cumulative Distribution Function for  
        the Binomial family of distributions.  
         
        Definition:  
       --------------------------------------------------------------------------  
        The Bin(n,p) distribution is the distribution of the number of  
        successes from n identical independent Bernoulli trials each with  
        success probability p. If random variable R is the number of  
        successes from such a set of Bernoulli trials, then the CDF F(r) is  
        the probability of r or less successes.  
         
        The Binomial distribution is discrete, defined for p in [0,1] and r  
        in {0,1,...,n}, so F(r) is a discrete function. This inverse CDF  
        function returns the smallest Whole r such that the F(r) equals or  
        exceeds the given CDF probability F. I.e. F(r) is treated as a step  
        function.  
         
        Algorithm:  
       --------------------------------------------------------------------------  
        r is found by direct summation of the Binomial PDFs until F is exceeded.  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_invIcdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_invIcdf", *args, **kwargs)
