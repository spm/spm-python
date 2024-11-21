from spm.__wrapper__ import Runtime


def spm_Ppdf(*args, **kwargs):
    """
      Probability Distribution Function (PDF) of Poisson distribution  
        FORMAT f = spm_Ppdf(x,l)  
         
        x - ordinates  
        l - Poisson mean parameter (lambda l>0) [Defaults to 1]  
        f - Poisson PDF  
       __________________________________________________________________________  
         
        spm_Ppdf implements the Probaility Distribution Function of the  
        Poisson distribution.  
          
        Definition:  
       --------------------------------------------------------------------------  
        The Poisson Po(l) distribution is the distribution of the number of  
        events in unit time for a stationary Poisson process with mean  
        parameter lambda=1, or equivalently rate 1/l. If random variable X is  
        the number of such events, then X~Po(l), and the PDF f(x) is  
        Pr({X=x}.  
         
        f(x) is defined for strictly positive l, given by: (See Evans et al., Ch31)  
         
                  { l^x * exp(-l) / x!          for r=0,1,...  
           f(r) = |  
                  {  0                          otherwise  
         
        Algorithm:  
       --------------------------------------------------------------------------  
        To avoid roundoff errors for large x (in x! & l^x) & l (in l^x),  
        computation is done in logs.  
         
        Normal approximation:  
       --------------------------------------------------------------------------  
        For large lambda the normal approximation Y~:~N(l,l) may be used.  
        With continuity correction this gives  
        f(x) ~=~ Phi((x+.5-l)/sqrt(l)) -Phi((x-.5-l)/sqrt(l));  
        where Phi is the standard normal CDF, and ~=~ means "appox. =".  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Ppdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Ppdf", *args, **kwargs)
