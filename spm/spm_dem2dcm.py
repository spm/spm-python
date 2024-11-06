from spm.__wrapper__ import Runtime


def spm_dem2dcm(*args, **kwargs):
    """
      Reorganisation of posteriors and priors into DCM format  
        FORMAT [DCM] = spm_dem2dcm(DEM)  
        FORMAT [DEM] = spm_dem2dcm(DEM,DCM)  
         
        DEM - structure array (hierarchicial model)  
        DCM - structure array (flat model)  
         
        -------------------------------------------------------------------------  
            DCM.M.pE - prior expectation of parameters  
            DCM.M.pC - prior covariances of parameters  
            DCM.Ep   - posterior expectations  
            DCM.Cp   - posterior covariance  
            DCM.F   - free energy  
         
        For hierarchical models (DEM.M) the first level with non-zero prior  
        variance on the parameters will be extracted.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dem2dcm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dem2dcm", *args, **kwargs)
