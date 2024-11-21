from spm.__wrapper__ import Runtime


def spm_mci_mfx(*args, **kwargs):
    """
      Mixed Effects Inference   
        FORMAT [MCI] = spm_mci_mfx (MCI)  
         
        MCI               Data structure containing fields:  
         
        .M{n}             Model for nth of N replications (e.g. subjects)  
        .U{n}             Inputs for nth replication  
        .Y{n}             Data for nth replication  
        .S                Second level model describing population mean, m, and   
                          precision, Lambda. The parameters in S.prior  
                          define the sufficient statistics of p(Lambda) (.a and .B)  
                          and p(m|Lambda) (.beta and.m)  
         
        .inference        'amc' or 'lgv' (default)  
        .total_its        Total number of samples per subject  
        .rinit            Proportion of samples to collect prior to use of  
                          Empirical (group) prior  
        .verbose          Show progress of optimisation   
        .update_obs_noise Update observation noise ? [yes/no] (1/0), default=1  
         
        The output fields are:   
         
        POSTERIOR SAMPLES:  
        .sm               [Nw x Nsamples] group random effect means, m  
        .sw               [Nw x N x Nsamples] subject random effects, w  
        .Ce               [Ny x Ny x Nsamples] Obs noise covariance samples  
        .postind          Indices for posterior (ie. excluding burn-in)  
         
        POSTERIOR MEANS:  
        .sm_mean          [Nw x 1] posterior mean over m  
        .sw_mean          [Nw x N] posterior mean over w  
         
        SUFFICIENT STATISTICS:  
        .noise            Parameters of p(Gamma|Y,w,v): .c0,.D0,.cN,.DN  
        .S.post           Parameters of p(Lambda|w) (.a and.B)   
                          and p(m|Lambda,w) (.beta and .m)  
         
        W.Penny, M Klein-Flugge and B Sengupta (2015) Mixed Effects Langevin  
        Monte Carlo, Submitted, 2015.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_mfx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_mfx", *args, **kwargs)
