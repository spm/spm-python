from spm.__wrapper__ import Runtime


def spm_mci_ais(*args, **kwargs):
    """
      Annealed Importance Sampling  
        FORMAT [post] = spm_mci_ais (mcmc,M,U,Y,vl)  
          
        mcmc      Optimisation parameters  eg.  
         
        .J        number of temperatures  
        .anneal   annealing schedule:  
                  'sigmoid', 'linear', 'nonlinear', 'log' or 'power'  
        .prop     type of proposal: 'lmc' or 'mh' (default)  
        .nprop    number of proposals at each temperature  
        .maxits   number of independent samples to produce  
         
        M         Model structure   
        U         Input structure  
        Y         Data   
        vl        Variational Laplace solution  
                      .Ep                 Posterior Mean  
                      .Cp                 Posterior Covariance  
                  If this field is specified then AIS starts sampling  
                  from the VL posterior. Otherwise from the model prior.  
         
        The function returns data structure 'post' with fields  
         
        .P                P(:,j) is jth posterior sample  
        .logev            approximation to log evidence  
        .logev_se         standard error thereof  
        .logev_lower      5th percentile thereof  
        .logev_upper      95th percentile thereof  
        .logev_resample   resampled log evidences  
        .traj             individual trajectories  
        .acc              acceptances  
        .logw             log of (unnormalised) importance weights  
        .q                normalised importance weights  
        .E                energy (negative log joint)  
        .beta             set of inverse temperatures  
         
        R Neal (2001) Annealed Importance Sampling. Statistics and  
        Computing, 11, 125-139.  
         
        This implementation uses the Matlab Parallel Computing toolbox  
        (see use of parfor instead of for below).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_ais.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_ais", *args, **kwargs)
