from spm.__wrapper__ import Runtime


def spm_invNcdf(*args, **kwargs):
    """
      Inverse Cumulative Distribution Function (CDF) for univariate Normal  
        FORMAT x = spm_invNcdf(F,u,v)  
         
        F - CDF (lower tail p-value)  
        u - mean              [Defaults to 0]  
        v - variance  (v>0)   [Defaults to 1]  
        x - ordinates of N(u,v) at which CDF F(x)=F  
       __________________________________________________________________________  
         
        spm_invNcdf implements the inverse of the Cumulative Distribution  
        Function (CDF) for the Normal (Gaussian) family of distributions.  
         
        Returns the variate x, such that Pr{X<x} = F for X~N(u,v), a  
        univariate random variable distributed Normally with mean u and  
        variance v.  
         
        Definition:  
       --------------------------------------------------------------------------  
        The CDF F(x) of a Normal distribution with mean u and variance v is  
        the probability that a random realisation X from this distribution  
        will be less than x. F(x)=Pr(X<=x) for X~N(u,v). The inverse CDF  
        returns the normal ordinate x for which the CDF is F. See Evans et  
        al., Ch29 for further definitions and variate relationships.  
         
        If X~N(u,v), then Z=(Z-u)/sqrt(v) has a standard normal distribution,  
        Z~N(0,1). The CDF of the standard normal distribution is known as  
        \Phi(z), its inverse as \Phi^{-1}(F).  
         
        Algorithm:  
       --------------------------------------------------------------------------  
        The CDF for a standard N(0,1) Normal distribution, \Phi(z), is  
        related to the error function by: (Abramowitz & Stegun, 26.2.29)  
         
              \Phi(z)      = 0.5 + erf(z/sqrt(2))/2  
        so  
         
              \Phi^{-1}(p) = sqrt(2) * erfinv(2*p-1)  
         
        where erfinv(.) is the inverse error function.  
         
        MATLAB's implementation of the inverse error function is used for  
        computation of z=\Phi^{-1}(F), the corresponding standard normal  
        variate, which converted to a variate x from a N(u,v) distribution by:  
              x = u+z*sqrt(v)  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_invNcdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_invNcdf", *args, **kwargs)
