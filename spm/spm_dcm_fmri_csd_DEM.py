from spm.__wrapper__ import Runtime


def spm_dcm_fmri_csd_DEM(*args, **kwargs):
    """
      Estimate parameters of a DCM using cross spectral fMRI densities  
        FORMAT DCM = spm_dcm_fmri_csd_DEM(DCM)  
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
         
        This routine estimates the parameters of a hierarchical model  
        of fMRI responses, using the complex cross spectra under stationarity  
        assumptions. The cross spectra are estimated from regional timeseries  
        (the nodes of the DCM graph) using a Bayesian multivariate autoregressive  
        model. The complex cross spectra are then fitted using linear systems  
        theory in frequency space, under the simple assumption that the observed  
        spectra are the predicted spectra plus some smooth Gaussian fluctuations  
        (noise). The characterisation of the model parameters can then be  
        examined in terms of directed transfer functions, spectral density and  
        crosscorrelation functions at the neuronal level - having accounted for  
        variations in haemodynamics at each node.  
         
        This scheming uses a hierarchical generative model of connectivity with  
        hierarchical constraints on the edges and therefore uses the expectation  
        and maximisation stepits of dynamic expectation maximisation. Here, the  
        hidden causes at the first level are the effective connectivity and the  
        hidden causes at the second level are the Lyapunov exponents or   
        eigenvalues of a symmetrical Jacobian or effective connectivity matrix:  
        see DEM_demo_modes_fMRI.m  
         
        see also: spm_dcm_estimate  
                  spm_dcm_fmri_csd  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_fmri_csd_DEM.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_fmri_csd_DEM", *args, **kwargs)
