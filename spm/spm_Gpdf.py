from spm.__wrapper__ import Runtime


def spm_Gpdf(*args, **kwargs):
    """
      Probability Density Function (PDF) of Gamma distribution  
        FORMAT f = spm_Gpdf(x,h,l)  
         
        x - Gamma-variate   (Gamma has range [0,Inf) )  
        h - Shape parameter (h>0)  
        l - Scale parameter (l>0)  
        f - PDF of Gamma-distribution with shape & scale parameters h & l  
       __________________________________________________________________________  
         
        spm_Gpdf implements the Probability Density Function of the Gamma  
        distribution.  
         
        Definition:  
       --------------------------------------------------------------------------  
        The PDF of the Gamma distribution with shape parameter h and scale l  
        is defined for h>0 & l>0 and for x in [0,Inf) by: (See Evans et al.,  
        Ch18, but note that this reference uses the alternative  
        parameterisation of the Gamma with scale parameter c=1/l)  
         
                  l^h * x^(h-1) exp(-lx)  
           f(x) = ----------------------  
                          gamma(h)  
         
        Variate relationships: (Evans et al., Ch18 & Ch8)  
       --------------------------------------------------------------------------  
        For natural (strictly +ve integer) shape h this is an Erlang distribution.  
         
        The Standard Gamma distribution has a single parameter, the shape h.  
        The scale taken as l=1.  
         
        The Chi-squared distribution with v degrees of freedom is equivalent  
        to the Gamma distribution with scale parameter 1/2 and shape parameter v/2.  
         
        Algorithm:  
       --------------------------------------------------------------------------  
        Direct computation using logs to avoid roundoff errors.  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Gpdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Gpdf", *args, **kwargs)
