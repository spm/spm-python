from spm.__wrapper__ import Runtime


def spm_dcm_fmri_nmm(*args, **kwargs):
    """
      Estimates parameters of a DCM (neural mass model) for fMRI data  
        FORMAT [DCM] = spm_dcm_fmri_nmm(P)  
          DCM - DCM structure or its filename  
         
        Expects  
       --------------------------------------------------------------------------  
        DCM.a                              % switch on endogenous connections  
        DCM.b                              % switch on bilinear modulations  
        DCM.c                              % switch on exogenous connections  
        DCM.U                              % exogenous inputs  
        DCM.Y.y                            % responses  
        DCM.Y.X0                           % confounds  
        DCM.Y.Q                            % array of precision components  
        DCM.n                              % number of regions  
        DCM.v                              % number of scans  
         
        Options  
       --------------------------------------------------------------------------  
        DCM.options.nmm                    % neural mass model  
        DCM.options.centre                 % mean-centre inputs  
        DCM.options.nograph                % graphical display  
        DCM.options.P                      % starting estimates for parameters  
        DCM.options.hidden                 % indices of hidden regions  
        DCM.options.maxnodes               % maximum number of (effective) nodes  
        DCM.options.maxit                  % maximum number of iterations  
        DCM.options.hE                     % expected precision of the noise  
        DCM.options.hC                     % variance of noise expectation  
         
        Evaluates:  
       --------------------------------------------------------------------------  
        DCM.M                              % Model structure  
        DCM.Ep                             % Condition means (parameter structure)  
        DCM.Cp                             % Conditional covariances  
        DCM.Vp                             % Conditional variances  
        DCM.Pp                             % Conditional probabilities  
        DCM.H1                             % 1st order hemodynamic kernels  
        DCM.H2                             % 2nd order hemodynamic kernels  
        DCM.K1                             % 1st order neuronal kernels  
        DCM.K2                             % 2nd order neuronal kernels  
        DCM.R                              % residuals  
        DCM.y                              % predicted data  
        DCM.T                              % Threshold for Posterior inference  
        DCM.Ce                             % Error variance for each region  
        DCM.F                              % Free-energy bound on log evidence  
        DCM.ID                             % Data ID  
        DCM.AIC                            % Akaike Information criterion  
        DCM.BIC                            % Bayesian Information criterion  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_fmri_nmm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_fmri_nmm", *args, **kwargs)
