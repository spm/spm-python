from spm.__wrapper__ import Runtime


def spm_spm_Bayes(*args, **kwargs):
    """
      Conditional parameter estimation of a General Linear Model  
        FORMAT [SPM] = spm_spm_Bayes(SPM)  
       __________________________________________________________________________  
         
        spm_spm_Bayes returns to voxels identified by spm_spm (ML parameter  
        estimation) to get conditional parameter estimates and ReML hyper-  
        parameter estimates.  These estimates use prior covariances, on the  
        parameters, from empirical Bayes.  These PEB prior variances come from  
        the hierarchical model that obtains by considering voxels as providing a  
        second level.  Put simply, the variance in parameters, over voxels, is  
        used as a prior variance from the point of view of any one voxel. The  
        error covariance hyperparameters are re-estimated in the light of these  
        priors.  The approach adopted is essentially a fully Bayesian analysis at  
        each voxel, using empirical Bayesian prior variance estimators over  
        voxels.  
         
        Each separable partition (i.e. session) is assigned its own  
        hyperparameter but within session covariance components are lumped  
        together, using their relative expectations over voxels.  This makes  
        things much more computationally efficient and avoids inefficient  
        voxel-specific multiple hyperparameter estimates.  
         
        spm_spm_Bayes adds the following fields to SPM:  
         
                                  ----------------  
         
         
          SPM.PPM.l      = session-specific hyperparameter means  
          SPM.PPM.Cb     = empirical prior parameter covariances  
          SPM.PPM.C      = conditional covariances of parameters  
          SPM.PPM.dC{i}  = dC/dl;  
          SPM.PPM.ddC{i} = ddC/dldl  
         
        The derivatives are used to compute the conditional variance of various  
        contrasts in spm_getSPM, using a Taylor expansion about the hyperparameter  
        means.  
         
         
                                  ----------------  
         
          SPM.VCbeta     - Handles of conditional parameter estimates  
          SPM.VHp        - Handles of hyperparameter estimates  
         
                                  ----------------  
         
        Cbeta_????.<ext>                     - conditional parameter images  
        These are 32-bit (float) images of the conditional estimates. The image  
        files are numbered according to the corresponding column of the  
        design matrix. Voxels outside the analysis mask (mask.<ext>) are given  
        value NaN.  
         
                                  ----------------  
         
        CHp_????.<ext>              - error covariance hyperparameter images  
        This is a 64-bit (double) image of the ReML error variance estimate.  
        for each separable partition (Session).  Voxels outside the analysis   
        mask are given value NaN.  
       __________________________________________________________________________  
          
        For single subject fMRI analysis there is an alternative function  
        using voxel-wise GLM-AR models that are spatially regularised  
        using the VB framework. This is implemented using spm_spm_vb.m.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_spm_Bayes.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_spm_Bayes", *args, **kwargs)
