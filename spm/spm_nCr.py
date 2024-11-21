from spm.__wrapper__ import Runtime


def spm_nCr(*args, **kwargs):
    """
      Combinatorics: n choose r, nCr  
        FORMAT c = spm_nCr(n,r)  
         
        n - Number of objects  
        r - Number of objects to choose  
        c - n choose r  
       __________________________________________________________________________  
         
        spm_nCr returns the number of ways of choosing r objects from a pool  
        of n objects, without replacement, order unimportant. Equivalently:  
        the number of ways of putting r objects into n indistinguishable urns  
        with exclusion. These are the Binomial coefficients of Pascal's  
        triangle:  
                   ( n )      n!  
                   |   | = ---------  
                   ( r )   r! (n-r)!  
         
        n & r must be whole numbers, with n>=r. Non-integer or out-of-range  
        arguments return zero as nCr. Non-scalar n & r must have the same  
        dimensons.  
         
        Algorithm:  
       --------------------------------------------------------------------------  
        For vary small n, nCr can be computed naively as the ratio of  
        factorials, using gamma(x+1) to return x!. For moderately sized n, n!  
        (& r! &/or (n-r)!) become very large, and naive computation isn't  
        possible. Direct computation is still possible upon noting that the  
        expression cancels down to the product of r fractions:  
         
                    n!       n   n-1         n-(r-1)  
                ---------  = - x --- x ... x -------  
                n! (n-r)!    r   r-1            1  
         
        Unfortunately this cunning computation (given at the end of this  
        function) is difficult to vectorise. Therefore we compute the log of  
        nCr as (ln(n!)-ln(r!)-ln((n-r)!), using the log-gamma special  
        function gammaln:  
         
          nCr = exp( gammaln(n+1) - gammaln(r+1) - gammaln(n-r+1) )  
         
        The result is rounded to cope with roundoff error for smaller values  
        of n & r. See Press et al., Sec6.1 for further details.  
         
        References  
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_nCr.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_nCr", *args, **kwargs)
