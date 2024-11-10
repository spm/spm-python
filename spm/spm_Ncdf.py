from spm.__wrapper__ import Runtime


def spm_Ncdf(*args, **kwargs):
    """
      Cumulative Distribution Function (CDF) for univariate Normal distributions  
        FORMAT F = spm_Ncdf(x,u,v)  
         
        x - ordinates  
        u - mean              [Defaults to 0]  
        v - variance  (v>0)   [Defaults to 1]  
        F - pdf of N(u,v) at x (Lower tail probability)  
       __________________________________________________________________________  
         
        spm_Ncdf implements the Cumulative Distribution Function (CDF) for  
        the Normal (Gaussian) family of distributions.  
         
        Definition:  
       --------------------------------------------------------------------------  
        The CDF F(x) of a Normal distribution with mean u and variance v is  
        the probability that a random realisation X from this distribution  
        will be less than x. F(x)=Pr(X<=x) for X~N(u,v). See Evans et al.,  
        Ch29 for further definitions and variate relationships.  
         
        If X~N(u,v), then Z=(Z-u)/sqrt(v) has a standard normal distribution,  
        Z~N(0,1). The CDF of the standard normal distribution is known as \Phi(z).  
         
        (KWorsley) For extreme variates with abs(z)>6 where z=(x-u)/sqrt(v), the  
        approximation \Phi(z) \approx exp(-z^2/2)/(z*sqrt(2*pi)) may be useful.  
         
        Algorithm:  
       --------------------------------------------------------------------------  
        The CDF for a standard N(0,1) Normal distribution, \Phi(z), is  
        related to the error function by: (Abramowitz & Stegun, 26.2.29)  
         
              \Phi(z) = 0.5 + erf(z/sqrt(2))/2  
         
        MATLAB's implementation of the error function is used for computation.  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Ncdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Ncdf", *args, **kwargs)
