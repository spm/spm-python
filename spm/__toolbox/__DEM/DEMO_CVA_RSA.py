from spm.__wrapper__ import Runtime


def DEMO_CVA_RSA(*args, **kwargs):
    """
      Canonical Variate Analysis and representational similarity analysis  
        FORMAT RSA = DEMO_CVA_RSA  
         
        output structure  
       --------------------------------------------------------------------------  
        RSA.C    - hypotheses matrices  
        RSA.c    - (orthogonalised) contrasts  
        RSA.W    - (second-order) canonical weights  
        RSA.X    - design matrix  
        RSA.Y    - data  
        RSA.X0   - confounds  
        RSA.F    - (BIC) log evidence  
       __________________________________________________________________________  
         
        This demonstration routine starts with a canonical covariates analysis in  
        which hypotheses are specified in terms of second-order matrices (of the  
        sort used in representational similarity analysis). This part  
        illustrates the inversion of a multivariate linear model over multiple  
        subjects, testing for the expression of multivariate responses under each  
        of three hypotheses. Furthermore, it illustrates the (Bayesian) model  
        comparison under the assumption that only one hypothesisis true.  
         
        The three hypotheses correspond to a main effect of a parametric variable  
        (e.g., the degree to which something is judged valuable), the main  
        effect of a categorical variable (e.g., big or small) and their  
        interaction. Note that this requires a specification in terms of  
        second-order hypothesis matrices that are not expressed in terms of  
        similarities per se. In other words, the second-order hypotheses are  
        assumed to be in the form of covariance matrices; as opposed to  
        correlation matrices.  
         
        This routine demonstrates the testing of hypothesis matrices with a rank  
        of one (corresponding to a T-contrast). However, the code has been  
        written to handle arbitrary hypothesis matrices (corresponding to F-  
        contrasts) that test a subspace of two or more dimensions.  
         
        To the extent that this reproduces the hypothesis testing of  
        representational similarity analysis, there is an important observation:  
        this analysis works for a single voxel. In other words, representational  
        similarity analysis is not an inherently multivariate approach.  
         
        This illustration deliberately mixes two (main) effects in equal measure,  
        within the same region of interest. This is to highlight the  
        inappropriate application of hypothesis selection; here demonstrated via  
        Bayesian model comparison using the Bayesian information criteria. In  
        other words, several hypotheses about a particular region could be true  
        at the same time.  
         
        We then revisit exactly the same problem (i.e., Bayesian model comparison  
        of covariance components of second-order responses) using variational  
        Laplace to estimate the contributions of each component of pattern  
        explicitly. This has the advantage of enabling parametric empirical Bayes  
        at the between subject level - and subsequent Bayesian model reduction.  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEMO_CVA_RSA.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEMO_CVA_RSA", *args, **kwargs)
