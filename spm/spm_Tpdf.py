from spm._runtime import Runtime


def spm_Tpdf(*args, **kwargs):
    """
      Probability Density Function (PDF) of Students t distribution  
        FORMAT f = spm_Tpdf(x,v)  
         
        x - t-ordinates  
        v - degrees of freedom (v>0, non-integer d.f. accepted)  
        f - PDF of t-distribution with v degrees of freedom (df) at points t  
       __________________________________________________________________________  
         
        spm_Tpdf implements the Probability Density Function of Students   
        t-distributions.  
         
        Definition:  
       --------------------------------------------------------------------------  
        The Student's t-distribution with v degrees of freedom is defined for  
        positive integer v and x in (-Inf,Inf), and has Probability Distribution  
        Function (PDF) f(x) given by: (See Evans et al., Ch37)  
         
                      gamma((v+1)/2)  
           f(x) = -----------------------  *  (1 + x^2/v) ^ -((v+1)/2  
                  sqrt(pi*v) * gamma(v/2)  
         
        This implementation is not restricted to whole (positive integer) df  
        v, rather it will compute for any df v>0.  
         
        Algorithm:  
       --------------------------------------------------------------------------  
        Direct computation using the beta function for  
              sqrt(pi)*gamma(v/2) / gamma((v+1)/2)  =  beta(v/2,1/2)  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Tpdf.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_Tpdf", *args, **kwargs)
