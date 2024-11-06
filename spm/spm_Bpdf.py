from spm.__wrapper__ import Runtime


def spm_Bpdf(*args, **kwargs):
    """
      Probability Density Function (PDF) of Beta distribution  
        FORMAT f = spm_Bpdf(x,v,w)  
         
        x   - Beta variates (Beta has range [0,1])  
        v   - Shape parameter (v>0)  
        w   - Shape parameter (w>0)  
        F   - PDF of Beta distribution with shape parameters [v,w] at points x  
       __________________________________________________________________________  
         
        spm_Bpdf implements the Probability Density Function for Beta distributions.  
         
        Definition:  
       --------------------------------------------------------------------------  
        The PDF of the Beta distribution shape parameters v & w, defined  
        for positive integer degrees of freedom v>0 & w>0, and for x in  
        [0,1] is given by: (See Evans et al., Ch5)  
         
                   x^(v-1) * (1-x)^(w-1)  
           f(x) = -----------------------  
                        beta(v,w)  
         
        Variate relationships:  
       --------------------------------------------------------------------------  
        Many: See Evans et al., Ch5  
         
        Algorithm:  
       --------------------------------------------------------------------------  
        Direct computation using logs and MATLAB's implementation of the log  
        beta function (betaln).  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Bpdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Bpdf", *args, **kwargs)
