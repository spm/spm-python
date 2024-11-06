from spm.__wrapper__ import Runtime


def spm_mci_pop(*args, **kwargs):
    """
      Population MCMC with Gaussian priors and proposals  
        FORMAT [P,logev,D,M] = spm_mci_pop (mcmc,M,U,Y)  
          
        mcmc      Optimisation parameters  eg.  
         
        .J        number of chains   
        .gprob    prob of global move  
        .nscale   number of scaling samples  
        .ntune    number of tuning samples  
        .nsamp    number samples (on avg) to return (per chain)  
        .remove_burn_in Remove scale and tune samples.  
        .init{j}  [Np x 1] Initial parameter vector for jth chain [optional]  
         
        M{i}      Data structure for i=1st or i=2nd model. 1st model  
                  is the larger model. Specifying two models is only   
                  necessary if you wish to do model switch integration.  
                  Each M structure should contain  
         
        .L        Name of log-likelihood function eg. 'spm_dcm_like'  
                      must take arguments P,M,U,Y  
        .pE       Prior mean  
        .pC       Prior covariance  
        .lambda1  Observation noise precision  
         
        For example, if ith model does not have variable k   
        one can set M{i}.pC(k,k)=1e-4;  
         
        U{i}    Input field for ith model (as standard)  
        Y       Data field  
         
        For each chain the function implements the Adaptive Monte Carlo (AMC)  
        algorithm which comprises three phases (i) scaling: proposal cov is   
        optimally scaled prior (same scaling for all params), (ii) tuning:   
        proposal cov is tuned using Robbins-Monro, (iii) sampling: the proposal  
        is unchanged. At each stage proposals follow Metropolis-Hastings.  
         
        The function returns  
         
        P{j}      Posterior samples from jth chain  
        logev     approximations to log evidence  
                  .pam    Prior Arithmetic Mean   
                  .phm    Posterior Harmonic Mean   
                  .ti     Thermodynamic Integration  
         
        For model switch integration logev.ti contains the log Bayes factor  
        for model 2 versus model 1  
         
        D         Diagnostics  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_pop.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_pop", *args, **kwargs)
