from spm.__wrapper__ import Runtime


def spm_dcm_fmri_check(*args, **kwargs):
    """
      Post-hoc diagnostics for DCM (bilinear or nonlinear) of fMRI data  
        FORMAT [DCM] = spm_dcm_fmri_check(DCM)  
          DCM     - DCM structure or its filename  
         
        FORMAT [GCM] = spm_dcm_fmri_check(GCM)  
          GCM     - Subjects x Models cell array of DCM structures or filenames  
         
        FORMAT [DCM] = spm_dcm_fmri_check(DCM, nograph, GCM)  
          DCM     - DCM structure or its filename  
          nograph - (Optional) if true, disables graphical output  
          GCM     - (Optional) full GCM array from which the DCM in P was sourced  
                    for use in graphics  
         
        This routine provides some diagnostics to ensure model inversion has  
        converged. It plots the predicted and observed responses over all regions  
        and provides the coefficient of determination - or percent variance  
        explained. This should normally be above 10%. An abnormally low  
        coefficient of determination is highlighted in red. Quantitatively, one  
        would normally expect to see one or more extrinsic (between source)  
        connections with the strength of 1/8 Hz or greater. If all the extrinsic  
        posterior expectations are below this value, then this suggests a failure  
        of convergence or that the data are very noisy (possibly due to using  
        very small regions of interest to summarise regional responses). Finally,  
        the posterior correlations among all parameters are shown in terms of a  
        correlation matrix. The number of effective parameters estimated is  
        reported in terms of the (KL) divergence between the posterior and  
        prior densities over parameters. This is divided by the log of the  
        number of observations, by appealing to the Bayesian information  
        criterion. The divergence corresponds to complexity or Bayesian  
        surprise. Normally, one would expect the posterior and prior to diverge  
        in a non-trivial fashion.  
         
        Posterior densities are shown as bars with 90% confidence intervals in  
        pink. An informed model inversion would normally provide posterior  
        densities with confidence intervals that are, for some connections,  
        displaced from prior expectations (at or around zero).  
         
        The following diagnostics are stored in the returned DCM:  
         
        DCM.diagnostics(1) - Percent variance explained  
        DCM.diagnostics(2) - Largest absolute parameter estimate  
        DCM.diagnostics(3) - Effective number of parameters estimated  
         
        This routine is compatible with DCM8, DCM10 and DCM12 files.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_fmri_check.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_fmri_check", *args, **kwargs)
