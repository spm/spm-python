from spm.__wrapper__ import Runtime


def spm_dcm_peb_con(*args, **kwargs):
    """
      Bayesian contrast of the parameters in a PEB model or BMA  
        FORMAT [P,c,v] = spm_dcm_peb_con(PEB, C, threshold, doplot)  
         
        Inputs:  
         
        PEB       - estimated PEB model or BMA of PEB models  
        C         - contrast vector or matrix (see below)  
        threshold - (optional) test statistic [default: 0]  
        doplot    - (optional) whether to plot results, default false  
         
        Outputs:  
          
        P         - probability that the contrast value is larger than the  
                    threshold  
        c,v       - mean and variance of the contrast, e.g. the probability of a  
                    difference between two connections  
         
        Specifying the contrast vector / matrix:  
         
        The contrast vector or matrix should be the same size as the parameters  
        in the PEB model (if shorter, it will be padded with zeros). The   
        parameters in matrix PEB.Ep are of dimension: [connections x covariates].  
        This matrix is vectorized in a BMA, by stacking the covariates on top of    
        one another. The elements of the contrast matrix define a linear mixture  
        of the parameters. For example, for a PEB model with two connections and   
        three covariates, the following contrast compares the first and second   
        connections of covariate one:  
         
        C = [1 0 0;  
            -1 0 0];  
         
        And the following contrast compares the effects of the second and third   
        covariates on the first connection:  
         
        C = [0 1 -1;  
             0 0  0];  
          
        Having defined the contrast matrix, call this function using:  
         
        [P,c,v] = spm_dcm_peb_con(PEB, C, 0, true);  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_peb_con.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_peb_con", *args, **kwargs)
