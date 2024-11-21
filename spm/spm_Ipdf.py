from spm.__wrapper__ import Runtime


def spm_Ipdf(*args, **kwargs):
    """
      Probability Distribution Function of Binomial distribution  
        FORMAT f = spm_Ipdf(x,n,p)  
         
        x - ordinates  
        n - Binomial n  
        p - Binomial p [Defaults to 0.5]  
        f - PDF  
       __________________________________________________________________________  
         
        spm_Ipdf returns the Probability (Distribution) Function (PDF) for  
        the Binomial family of distributions.  
         
        Definition:  
       --------------------------------------------------------------------------  
        The Bin(n,p) distribution is the distribution of the number of  
        successes from n identical independent Bernoulli trials each with  
        success probability p. If random variable X is the number of  
        successes from such a set of Bernoulli trials, then the PDF f(x) is  
        Pr{X=x}, defined for whole n (i.e. non-negative integer n) and  
        p in [0,1], given by: (See Evans et al., Ch6)  
         
                  { nCx * p^x * (1-p)^(n-x)     for x=0,1,...,n  
           f(x) = |  
                  {  0                          otherwise  
         
        where nCx is the Binomial coefficient "n-choose-x", given by n!/(x!(n-x)!).  
         
        Algorithm:  
       --------------------------------------------------------------------------  
        For vary small n, nCx can be computed naively as the ratio of  
        factorials, using gamma(n+1) to return n!. For moderately sized n, n!  
        (& x! &/or (n-x)!) become very large, and naive computation isn't  
        possible. Direct computation is always possible upon noting that the  
        expression cancels down to the product of x fractions:  
         
                    n!       n   n-1         n-(x-1)  
                ---------  = - x --- x ... x -------  
                n! (n-x)!    x   x-1            1  
         
        Unfortunately this cunning computation (given at the end of this  
        function) is difficult to vectorise. Therefore we compute via the log  
        of nCx as e^(ln(n!)-ln(x!)-ln((n-x)!), using the special function  
        gammaln:  
         
              nCx = exp( gammaln(n+1) - gammaln(x+1) - gammaln(n-x+1) )  
         
        The result is rounded to cope with roundoff error for smaller values  
        of n & x. See Press et al., Sec6.1 for further details.  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Ipdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Ipdf", *args, **kwargs)
