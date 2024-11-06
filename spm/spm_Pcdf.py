from spm.__wrapper__ import Runtime


def spm_Pcdf(*args, **kwargs):
    """
      Cumulative Distribution Function (PDF) of Poisson distribution  
        FORMAT F = spm_Pcdf(x,l)  
         
        x - ordinates  
        l - Poisson mean parameter (lambda l>0) [Defaults to 1]  
        F - Poisson CDF  
       __________________________________________________________________________  
         
        spm_Pcdf implements the Cumulative Distribution Function of the  
        Poisson distribution.  
          
        Definition:  
       --------------------------------------------------------------------------  
        The Poisson Po(l) distribution is the distribution of the number of  
        events in unit time for a stationary Poisson process with mean  
        parameter lambda=1, or equivalently rate 1/l. If random variable X is  
        the number of such events, then X~Po(l), and the CDF F(x) is  
        Pr({X<=x}.  
         
        F(x) is defined for strictly positive l, given by: (See Evans et al., Ch31)  
         
                  { 0                                         for x<0  
                  |    _ floor(x)  
           f(rx = |    >      l^i * exp(-l) / i!)             for x>=0  
                  {    - i=0  
         
        Algorithm:  
       --------------------------------------------------------------------------  
        F(x), the CDF of the Poisson distribution, for X~Po(l), is related  
        to the incomplete gamma function, by:  
         
           F(x) = 1 - gammainc(l,x+1) (x>=0)  
         
        See Press et al., Sec6.2 for further details.  
         
        Normal approximation:  
       --------------------------------------------------------------------------  
        For large lambda the normal approximation Y~:~N(l,l) may be used.  
        With continuity correction this gives  
        F(x) ~=~ Phi((x+.5-l)/sqrt(l))  
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Pcdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Pcdf", *args, **kwargs)
