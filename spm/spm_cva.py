from spm.__wrapper__ import Runtime


def spm_cva(*args, **kwargs):
    """
      Canonical Variate Analysis  
        FORMAT [CVA] = spm_cva(Y,X,X0,c,[U])  
        Y            - data  
        X            - design  
        X0           - null space  
        c            - contrast weights  
        U            - dimension reduction (projection matrix)  
                     - or number to retain  
          
          
        CVA.c        - contrast weights  
        CVA.X        - contrast subspace  
        CVA.Y        - whitened and adjusted data  
        CVA.X0       - null space of contrast  
          
        CVA.V        - canonical vectors  (data)  
        CVA.v        - canonical variates (data)  
        CVA.W        - canonical vectors  (design)  
        CVA.w        - canonical variates (design)  
        CVA.C        - canonical contrast (design)  
          
        CVA.r        - canonical correlations  
        CVA.chi      - Chi-squared statistics testing D >= i  
        CVA.cva      - canonical value  
        CVA.df       - d.f.  
        CVA.p        - p-values  
         
        CVA.bic      - Bayesian Information Criterion   
        CVA.aic      - Akaike Information Criterion  
         
       __________________________________________________________________________  
          
        CVA uses the generalised eigenvalue solution to the treatment and  
        residual sum of squares and products of a general linear model. The  
        eigenvalues (i.e., canonical values), after transformation, have a  
        chi-squared distribution and allow one to test the null hypothesis that  
        the mapping is D or more dimensional. The first p-value is formally  
        identical to that obtained using Wilks' Lambda and tests for the   
        significance of any mapping.  
          
        This routine uses the current contrast to define the subspace of interest  
        and treats the remaining design as uninteresting. Conventional results  
        for the canonical values are used after the data (and design matrix) have  
        been whitened; using the appropriate ReML estimate of non-sphericity.  
          
        This function also computes the LogBayesFactor for testing the hypothesis  
        that the latent dimension (number of sig. canonical vectors) is i versus   
        zero: Two approximations are given: CVA.bic(i) and CVA.aic(i).   
        These LogBFs can then be used for group inference - see Jafarpour et al.  
                       
        References:  
          
        Characterizing dynamic brain responses with fMRI: a multivariate  
        approach. Friston KJ, Frith CD, Frackowiak RS, Turner R. NeuroImage. 1995  
        Jun;2(2):166-72.  
         
        A multivariate analysis of evoked responses in EEG and MEG data. Friston  
        KJ, Stephan KM, Heather JD, Frith CD, Ioannides AA, Liu LC, Rugg MD,  
        Vieth J, Keber H, Hunter K, Frackowiak RS. NeuroImage. 1996 Jun;  
        3(3):167-174.  
         
        Population level inference for multivariate MEG analysis. Jafarpour A,  
        Barnes G, Fuentemilla Lluis, Duzel E, Penny WD. PLoS One. 2013.  
        8(8): e71305  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_cva.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cva", *args, **kwargs)
