from spm.__wrapper__ import Runtime


def spm_dcm_nvc(*args, **kwargs):
    """
      Specify and estimate a DCM for multimodal fMRI and M/EEG  
        FORMAT [DCM] = spm_dcm_nvc(P)  
         
        Input:  
        -------------------------------------------------------------------------  
        P{1} - SPM structure or location of SPM.mat  
        P{2} - Cell array of VOI filenames (the same order as sources in EEG DCM)  
        P{3} - Location of DCM for M/EEG .mat file or DCM structure  
        P{4} - Model specification for neurovascular coupling (NVC) mechanisms  
        P{5} - Which neuronal populations should drive haemodynamics   
        P{6} - Which fMRI experimental conditions to include  
        P{7} - DCM options  
         
        Where:  
         
        P{4} - A cell array of strings with three elements:  
                 
          P{4}{1} - 'pre', 'post' or decomposed ('de') neuronal signals excite   
                     NVC. Decomposed means activity is grouped into intrinsic-  
                     inhibitory, intrinisic-excitatory and extrinsic-excitatory.  
          P{4}{2} - NVC has the same ('s') or different ('d') parameters for all  
                     regions.   
          P{4}{3} - extrinsic and intrinsic ('ext') or only intrinsic ('int')   
                     neuronal activity contributes to regional BOLD   
                     (for 'post', this should be 'na').  
             
          Supported options:  
          {'pre','d','int'},{'pre','s','int'}, {'pre','d','ext'},{'pre','s','ext'},  
          {'de','d', 'int'},{'de','d','exc'},  {'de','s','int'}, {'de','s','exc'},  
          {'post','d','na'},{'post','s','na'};  
         
          Example: P{4} = {'pre', 's', 'int'} means presynaptic neuronal drive  
          (from intrinsic connections only) inputs to a model of neurovascular  
          coupling that has the same parameters for all regions.  
         
        P{5} - Which neuronal populations should drive haemodynamics, by setting  
          ones or zeros in a vector ordered:  
          [superficial pyramidal, inhibitory, excitatory, deep pyramidal]  
          (default is [1 1 1 1]).  
         
          Example: [1 0 1 1] means no NVC drive from inhibitory populations.  
         
        P{6} - Binary vector indicating which experimental conditions to include.  
         
        P{7} - options structure for DCM for fMRI:    
           options.name                   % name for the DCM  
           options.maxit                  % maximum number of iterations  
           options.hE                     % expected precision of the noise  
           options.hC                     % variance of noise expectation  
           options.TE                     % echo time (default: 0.04)  
         
        Evaluates:  
        -------------------------------------------------------------------------  
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
         
        Notes on parameters:  
        -------------------------------------------------------------------------  
        This scheme estimates DCM.H (haemodynamic parameters) and DCM.J  
        (neurovascular coupling parameters):  
          
        DCM.Ep.H.transit - transit time (t0)  
        DCM.Ep.H.decay   - signal decay d(ds/dt)/ds)  
        DCM.Ep.H.epsilon - ratio of intra- to extra-vascular components of the  
                           gradient echo signal  
         
        DCM.Ep.J - neurovascular coupling parameters. The dimension depends upon   
        the requested model specification. For p populations and n regions:  
         
        P{7} (DCM.model)        dim(J)   notes  
        =========================================  
        {'pre'  'd' 'int'}      [p n]        
        {'pre'  's' 'int'}      [p 1]  
        {'pre'  'd' 'ext'}      [p n]  
        {'pre'  's' 'ext'}      [p 1]  
        {'de'   's' 'int}       [p 2]    dim2: intrinsic inhibitory, excitatory  
        {'de'   's' 'ext'}      [p 3]    dim2: intrinsic inhibitory, excitatory, extrinsic   
        {'de'   'd' 'int}       [p 2 n]  dim2: intrinsic inhibitory, excitatory  
        {'de'   'd' 'ext'}      [p 3 n]  dim2: intrinsic inhibitory, excitatory, extrinsic   
        {'post' 's' 'na'}       [p 1]  
        {'post' 'd' 'na'}       [p n]  
         
       __________________________________________________________________________  
        Jafarian, A., Litvak, V., Cagnan, H., Friston, K.J. and Zeidman, P., 2019.  
        Neurovascular coupling: insights from multi-modal dynamic causal modelling  
        of fMRI and MEG. arXiv preprint arXiv:1903.07478.  
         
        Friston, K.J., Preller, K.H., Mathys, C., Cagnan, H., Heinzle, J., Razi, A.  
        and Zeidman, P., 2017. Dynamic causal modelling revisited. Neuroimage.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/NVC/spm_dcm_nvc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_nvc", *args, **kwargs)
