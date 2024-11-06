from spm.__wrapper__ import Runtime


def spm_est_non_sphericity(*args, **kwargs):
    """
      Non-sphericity estimation using ReML  
        FORMAT [xVi, mask] = spm_est_non_sphericity(SPM)  
          
        Required fields of SPM structure (see spm_spm):  
        SPM.xY.VY  - nScan x 1 struct array of file handles  
        SPM.xX     - structure containing design matrix information  
        SPM.xX.W   - optional whitening/weighting matrix  
        SPM.xVi    - structure describing intrinsic non-sphericity  
        SPM.xM     - structure containing masking information  
          
        Return xVi from SPM.xVi with extra fields:  
        xVi.V      - estimated non-sphericity, trace(V) = rank(V)  
        xVi.h      - hyperparameters  xVi.V = xVi.h(1)*xVi.Vi{1} + ...  
        xVi.Cy     - spatially whitened <Y*Y'> (used by ReML to estimate h)  
          
        mask       - logical array of voxels within analysis mask  
       __________________________________________________________________________  
         
        In a first pass, voxels over which non-sphericity will be estimated are  
        selected using an 'effects of interest' F-contrast (can be specified in   
        SPM.xVi.Fcontrast) and critical threshold taken from SPM defaults  
        stats.<modality>.UFp.  
        The sample covariance matrix (xVi.Cy) is then estimated by pooling over  
        these voxels, assuming V is constant over them.  
        Finally, SPM will invoke ReML to estimate hyperparameters (xVi.h) of an  
        array of non-sphericity components (xVi.Vi), providing a high precise  
        estimate of the non-sphericity matrix (xVi.V).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_est_non_sphericity.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_est_non_sphericity", *args, **kwargs)
