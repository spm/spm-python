from spm.__wrapper__ import Runtime


def spm_Npdf(*args, **kwargs):
    """
      Probability Density Function (PDF) of univariate Normal distribution  
        FORMAT f = spm_Npdf(x,u,v)  
         
        x - ordinates  
        u - mean              [Defaults to 0]  
        v - variance  (v>0)   [Defaults to 1]  
        f - pdf of N(u,v) at x  
       __________________________________________________________________________  
         
        spm_Npdf returns the Probability Density Function (PDF) for the  
        univariate Normal (Gaussian) family of distributions.  
         
        Definition:  
       --------------------------------------------------------------------------  
        Let random variable X have a Normal distribution with mean u and  
        variance v, then Z~N(u,v). The Probability Density Function (PDF) of  
        the Normal (sometimes called Gaussian) family is f(x), defined on all  
        real x, given by: (See Evans et al., Ch29)  
         
                        1           ( (x-u)^2 )  
           f(r) = ------------ x exp| ------  |  
                  sqrt(v*2*pi)      (   2v    )  
         
        The PDF of the standard Normal distribution, with zero mean and unit  
        variance, Z~N(0,1), is commonly referred to as \phi(z).  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Npdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Npdf", *args, **kwargs)
