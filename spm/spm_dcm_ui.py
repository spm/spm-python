from spm.__wrapper__ import Runtime


def spm_dcm_ui(*args, **kwargs):
    """
      User interface for Dynamic Causal Modelling (DCM)  
        FORMAT spm_dcm_ui('specify')  
        FORMAT spm_dcm_ui('estimate')  
        FORMAT spm_dcm_ui('search')  
        FORMAT spm_dcm_ui('optimise')  
        FORMAT spm_dcm_ui('review')  
        FORMAT spm_dcm_ui('compare')  
        FORMAT spm_dcm_ui('average (BPA)')  
        FORMAT spm_dcm_ui('average (BMA)')  
         
        * Specify a new model  
        * Estimate a specified model  
        * Review a previously estimated model  
        * Compare two or more estimated models  
        * Produce an aggregate model using Bayesian averaging  
         
        DCM structure, as saved in DCM_???.mat:  
         
          DCM.M      - model  specification structure (see spm_nlsi)  
          DCM.Y      - output specification structure (see spm_nlsi)  
          DCM.U      - input  specification structure (see spm_nlsi)  
          DCM.Ep     - posterior expectations (see spm_nlsi)  
          DCM.Cp     - posterior covariances (see spm_nlsi)  
          DCM.a      - intrinsic connection matrix  
          DCM.b      - input-dependent connection matrix  
          DCM.c      - input connection matrix  
          DCM.Pp     - posterior probabilities  
          DCM.Vp     - variance of parameter estimates  
          DCM.H1     - 1st order Volterra Kernels - hemodynamic  
          DCM.K1     - 1st order Volterra Kernels - neuronal  
          DCM.R      - residuals  
          DCM.y      - predicted responses  
          DCM.xY     - original response variable structures  
          DCM.T      - threshold for inference based on posterior p.d.f  
          DCM.v      - Number of scans  
          DCM.n      - Number of regions  
         
       __________________________________________________________________________  
         
        DCM  is a  causal  modelling  procedure  for dynamical  systems  in which  
        causality  is inherent  in the  differential equations  that  specify the  
        model.  The basic idea  is to treat the system of interest,  in this case  
        the brain,  as an  input-state-output  system.  By perturbing  the system  
        with  known  inputs,  measured  responses  are used to  estimate  various  
        parameters that govern the evolution of brain states.  Although there are  
        no  restrictions  on  the  parameterisation  of  the  model,  a  bilinear  
        approximation affords a simple  re-parameterisation in terms of effective  
        connectivity.  This effective connectivity can be latent or intrinsic or,  
        through  bilinear  terms,  model  input-dependent  changes  in  effective  
        connectivity.   Parameter  estimation   proceeds  using  fairly  standard  
        approaches to system identification that rest upon Bayesian inference.  
          
        Dynamic  causal  modelling   represents  a   fundamental  departure  from  
        conventional   approaches   to   modelling   effective   connectivity  in  
        neuroscience.  The critical distinction between DCM and other approaches,  
        such as  structural equation  modelling  or  multivariate  autoregressive  
        techniques is that the input is treated as known, as opposed to stochastic.  
        In this sense DCM is much closer to conventional analyses of neuroimaging  
        time series  because the causal  or explanatory  variables enter as known  
        fixed quantities.  The use of designed and known inputs in characterising  
        neuroimaging data  with the general linear model or DCM is a more natural  
        way to  analyse data  from  designed  experiments.  Given  that  the vast  
        majority  of imaging  neuroscience  relies  upon designed  experiments we  
        consider DCM a potentially useful complement to existing techniques.    
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_ui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_ui", *args, **kwargs)
