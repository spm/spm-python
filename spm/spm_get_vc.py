from spm._runtime import Runtime


def spm_get_vc(*args, **kwargs):
    r"""
      Generate error covariance components for factorial designs  
        FORMAT Vi = spm_get_vc(I,factor)  
        I         - n x m matrix of factor level indicators  
                    I(n,i) is the level of factor i for observation n  
        factor(i) - structure array of sphericity assumptions for each factor  
        .variance - 1 for different variance among levels of factor i  
        .dept     - 1 for dependencies within levels of factor i  
         
        Vi        - cell vector of covariance components  
       __________________________________________________________________________  
         
        spm_get_vc generates variance components for a given design. For each  
        factor, the user specifies whether its levels have identical variances  
        and are independent. The individual components for each factor are  
        combined into covariance components by using the Kronecker tensor  
        product. If there are unequal number of observations at different levels,  
        the function specifies covariance components for a full factorial design  
        first and subsequently removes unwanted rows and columns from the  
        covariance matrices.  
         
        The functionality of spm_get_vc is similar to that of spm_non_sphericity.  
        The difference is that spm_get_vc can accommodate any number of factors  
        and is more general, because it can cope with different number of  
        observations under different levels of a factor.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_get_vc.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_get_vc", *args, **kwargs)
