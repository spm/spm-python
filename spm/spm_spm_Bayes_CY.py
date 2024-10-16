from spm.__wrapper__ import Runtime


def spm_spm_Bayes_CY(*args, **kwargs):
  """  Estimation of the average sample covariance of whole-brain data.  
     
    SPM - Structure (see spm_spm.m)  
    CY  - Matrix of dimension [P x P] where P is the number of volumes  
   __________________________________________________________________________  
     
    Normalisation (and where appropriate, temporal pre-whitening) are   
    performed prior to estimation. Voxels are included that exceed a liberal  
    statistical threshold, by default p < 0.001 uncorrected for effects of  
    interest. The resulting matrix is used in spm_spm_Bayes.m.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_spm_Bayes_CY.m)
  """

  return Runtime.call("spm_spm_Bayes_CY", *args, **kwargs)
