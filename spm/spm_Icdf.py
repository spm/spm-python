from spm.__wrapper__ import Runtime


def spm_Icdf(*args, **kwargs):
    """
      Cumulative Distribution Function (CDF) of Binomial Bin(n,p) distribution  
        FORMAT F = spm_Icdf(x,n,p)  
         
        x - ordinate  
        n - Binomial n  
        p - Binomial p [Defaults to 0.5]  
        F - CDF  
       __________________________________________________________________________  
         
        spm_Icdf returns the Cumulative Distribution Function for the  
        Binomial family of distributions.  
         
        Definition:  
       --------------------------------------------------------------------------  
        The Bin(n,p) distribution is the distribution of the number of  
        successes from n identical independent Bernoulli trials each with  
        success probability p. If random variable X is the number of  
        successes from such a set of Bernoulli trials, then the CDF F(x) is  
        Pr{X<=x}, the probability of x or less successes.  
         
        The Binomial CDF is defined for whole n (i.e. non-negative integer n)  
        and p in [0,1], given by: (See Evans et al., Ch6)  
         
                  { 0                                         for x<0  
                  |    _ floor(x)  
           F(x) = |    >      nCi * p^i * (1-p)^(n-i)         for 0<=x<=n  
                  |    - i=0  
                  { 1                                         for x>n  
         
        where nCx is the Binomial coefficient "n-choose-x", given by n!/(x!(n-x)!)  
         
        Normal approximation:  
       --------------------------------------------------------------------------  
        For (npq>5 & 0.1<=p<=0.9) | min(np,nq)>10 | npq>25 the Normal  
        approximation to the Binomial may be used:  
              X~Bin(n,p),  X~:~N(np,npq)              ( ~:~ -> approx. distributed as)  
        where q=1-p. With continuity correction this gives:  
              F(x) \approx \Phi((x+0.5-n*p)/sqrt(n*p*q))  
        for Phi the standard normal CDF, related to the error function by  
              \Phi(x) = 0.5+0.5*erf(x/sqrt(2))  
         
        Algorithm:  
       --------------------------------------------------------------------------  
        F(x), the CDF of the Binomial distribution, for X~Bin(n,p), is related  
        to the incomplete beta function, by:  
         
           F(x) = 1 - betainc(p,x+1,n-x) (0<=x<n)  
         
        See Abramowitz & Stegun, 26.5.24; and Press et al., Sec6.1 for  
        further details.  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Icdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Icdf", *args, **kwargs)
