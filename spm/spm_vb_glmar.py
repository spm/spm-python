from spm.__wrapper__ import Runtime


def spm_vb_glmar(*args, **kwargs):
    """
      Variational Bayes for GLM-AR modelling in a block of fMRI  
        FORMAT [block] = spm_vb_glmar (Y,block)  
         
        Y     -  [T x N] time series with T time points, N voxels  
         
        block -  data structure containing the following fields:  
         
                 .X              [T x k] the design matrix  
                 .p              order of AR model  
                 .D              [N x N] spatial precision matrix  
                                 (see spm_vb_set_priors.m)  
         
                 The above fields are mandatory. The fields below are  
                 optional or are filled in by this function.  
         
                 OPTIMISIATION PARAMETERS:  
         
                 .tol            termination tolerance (default = 0.01% increase in F)  
                 .maxits         maximum number of iterations (default=4)  
                 .verbose        '1' for description of actions (default=1)  
                 .update_???     set to 1 to update parameter ??? (set to 0 to fix)  
                                 eg. update_alpha=1; % update prior precision on W  
         
                 ESTIMATED REGRESSION COEFFICIENTS:  
         
                 .wk_mean        [k x N] VB regression coefficients  
                 .wk_ols         [k x N] OLS "  "  
                 .w_cov          N-element cell array with entries [k x k]  
                 .w_dev          [k x N] standard deviation of regression coeffs  
         
                 ESTIMATED AR COEFFICIENTS:  
         
                 .ap_mean        [p x N] VB AR coefficients  
                 .ap_ols         [p x N] OLS AR coefficients  
                 .a_cov          N-element cell array with entries [p x p]  
         
                 ESTIMATED NOISE PRECISION:  
         
                 .b_lambda       [N x 1] temporal noise precisions  
                 .c_lambda  
                 .mean_lambda  
         
                 MODEL COMPARISON AND COEFFICIENT RESELS:  
         
                 .gamma_tot      [k x 1] Coefficient RESELS  
                 .F              Negative free energy (used for model selection)  
                 .F_record       [its x 1] record of F at each iteration  
                 .elapsed_seconds  estimation time  
                 PRIORS:  
         
                 .b_alpha        [k x 1] spatial prior precisions for W  
                 .c_alpha  
                 .mean_alpha  
         
                 .b_beta         [p x 1] spatial prior precisions for AR  
                 .c_beta  
                 .mean_beta  
         
                 .b              [k x N] prior precision matrix  
         
                 HYPERPRIORS:  
         
                 .b_alpha_prior   priors on alpha  
                 .c_alpha_prior  
         
                 .b_beta_prior    priors on beta  
                 .c_beta_prior  
         
                 .b_lambda_prior  priors on temporal noise precisions  
                 .c_lambda_prior  
         
                 There are other fields that are used internally  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_vb_glmar.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vb_glmar", *args, **kwargs)
