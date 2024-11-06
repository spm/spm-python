from spm.__wrapper__ import Runtime


def spm_dcm_fmri_mar(*args, **kwargs):
    """
      Estimate parameters of a DCM using a MAR model of temporal dependencies  
        FORMAT DCM = spm_dcm_fmri_mar(DCM)  
          DCM - DCM structure  
         
        Expects  
       --------------------------------------------------------------------------  
        DCM.a                              % switch on endogenous connections  
        DCM.b                              % switch on bilinear modulations  
        DCM.c                              % switch on exogenous connections  
        DCM.d                              % switch on nonlinear modulations  
        DCM.U                              % exogenous inputs  
        DCM.Y.y                            % responses (over time)  
        DCM.n                              % number of regions  
        DCM.v                              % number of scans  
         
        This routine estimates the (A and C) parameters of a dynamic causal model  
        of fMRI responses, using MAR coefficients under stationarity  
        assumptions. The coefficients are estimated from regional timeseries  
        (the nodes of the DCM graph) using a Bayesian multivariate autoregressive  
        model. The coefficients are then fitted using linear systems  
        theory in coefficient space, under the simple assumption that the observed  
        spectra are the predicted spectra plus some smooth Gaussian fluctuations  
        (noise). The characterisation of the model parameters can then be  
        examined in terms of directed transfer functions, spectral density and  
        crosscorrelation functions at the neuronal level - having accounted for  
        variations in haemodynamics at each node.  
         
        Note that neuronal fluctuations are not changes in synaptic activity or  
        depolarisation per se but the fluctuations in the power of underlying  
        neuronal dynamics. As such, they have much slower time constants than the  
        neuronal dynamics.  
         
        see also: spm_dcm_estimate  
                  spm_dcm_fmri_csd  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_fmri_mar.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_fmri_mar", *args, **kwargs)
