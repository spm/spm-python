from spm.__wrapper__ import Runtime


def spm_mci_mfx_dynamic(*args, **kwargs):
    """
      Mixed Effects Inference for Dynamical Systems  
        FORMAT [MCI] = spm_mci_mfx_dynamic (MCI)  
         
        MCI               Data structure containing fields:  
         
        .M{n}             Model for nth of N replications (e.g. subjects)  
        .U{n}             Inputs for nth replication  
        .Y{n}             Data for nth replication  
        .fixed            Gaussian prior (.pE and .pC) over FFX  
        .S                Second level model describing population mean, m, and   
                          precision, Lambda. The parameters in S.prior  
                          define the sufficient statistics of p(Lambda) (.a and .B)  
                          and p(m|Lambda) (.beta and.m)  
        .total_its        Total number of samples per subject  
        .rinit            Proportion of samples to collect prior to use of  
                          Empirical (group) prior  
        .verbose          Show progress of optimisation  
         
        KNOWN, FIXED or RANDOM EFFECTS:  
        The initial states, flow and output   
        parameters can be fixed or random effects or take on known values:  
         
        .assign.init_par  'fixed', 'random' or 'known'  
        .assign.flow_par  'fixed', 'random' or 'known'  
        .assign.out_par   'fixed', 'random' or 'known'  
         
        .pinit0           Initial values of initial state parameters  
                          [Ninit x 1] for fixed, [Ninit x N] for random  
        .pflow0           Initial values of flow parameters  
                          [Nflow x 1] for fixed, [Nflow x N] for random  
        .pout0            Initial values of output parameters  
                          [Nout x 1] for fixed, [Nout x N] for random  
         
        .update_obs_noise Update observation noise, Gamma ? [yes/no] (1/0), default=1  
        .verbose          Show progress of optimisation   
         
        The output fields are:   
         
        POSTERIOR SAMPLES:  
        .sv               [Nv x Nsamples] group fixed effects samples, v  
        .sm               [Nw x Nsamples] group random effect means, m  
        .sw               [Nw x N x Nsamples] subject random effects, w  
        .Ce               [Ny x Ny x Nsamples] Obs noise covariance samples  
        .postind          Indices for posterior (ie. excluding burn-in)  
         
        POSTERIOR MEANS:  
        .sv_mean          [Nv x 1] posterior mean over v  
        .sm_mean          [Nw x 1] posterior mean over m  
        .sw_mean          [Nw x N] posterior mean over w  
         
        For Dynamical Systems models:  
        .pinit            Estimated initial states  
        .pflow            Estimated flow  
        .pout             Estimated output params  
         
        SUFFICIENT STATISTICS:  
        .noise            Parameters of p(Gamma|Y,w,v): .c0,.D0,.cN,.DN  
        .S.post           Parameters of p(Lambda|w) (.a and.B)   
                          and p(m|Lambda,w) (.beta and .m)  
         
        W.Penny, M Klein-Flugge and B Sengupta (2015) Mixed Effects Langevin  
        Monte Carlo, Submitted, 2015.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_mfx_dynamic.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_mfx_dynamic", *args, **kwargs)
