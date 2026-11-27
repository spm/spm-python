from spm._runtime import Runtime


def spm_spm_Bayes_CY(*args, **kwargs):
    r"""
      Estimation of the average sample covariance of whole-brain data.  
         
        SPM - Structure (see spm_spm.m)  
        CY  - Matrix of dimension [P x P] where P is the number of volumes  
       __________________________________________________________________________  
         
        Normalisation (and where appropriate, temporal pre-whitening) are   
        performed prior to estimation. Voxels are included that exceed a liberal  
        statistical threshold, by default p < 0.001 uncorrected for effects of  
        interest. The resulting matrix is used in spm_spm_Bayes.m.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_spm_Bayes_CY.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_spm_Bayes_CY", *args, **kwargs)
