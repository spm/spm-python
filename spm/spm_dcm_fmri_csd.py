from spm.__wrapper__ import Runtime


def spm_dcm_fmri_csd(*args, **kwargs):
    """
      Estimate parameters of a DCM using cross spectral fMRI densities  
        FORMAT DCM = spm_dcm_fmri_csd(DCM)  
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
        of fMRI responses, using the complex cross spectra under stationarity  
        assumptions. The cross spectra are estimated from regional timeseries  
        (the nodes of the DCM graph) using a Bayesian multivariate autoregressive  
        model. The complex cross spectra are then fitted using linear systems  
        theory in frequency space, under the simple assumption that the observed  
        spectra are the predicted spectra plus some scale free fluctuations  
        (noise). The characterisation of the model parameters can then be  
        examined in terms of directed transfer functions, spectral density and  
        crosscorrelation functions at the neuronal level - having accounted for  
        variations in haemodynamics at each node.  
         
        NB: if DCM.Y.y{i} is a cell array of multiple time series (e.g., sessions  
        or subjects), this routine will use DCM.b  as constraints on the  
        connectivity parameters that can change over sessions. The posterior  
        estimates in DCM.Ep.B  then correspond to the session specific deviations  
        from the average in DCM.Ep.A. The remaining results  pertain to the  
        average connectivity.  This facility can be used to test for between  
        session (or subject) effects with a subsequent application of parametric  
        empirical Bayes (PEB), applied to the  field 'B'.  
         
        see also: spm_dcm_estimate  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_fmri_csd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_fmri_csd", *args, **kwargs)
