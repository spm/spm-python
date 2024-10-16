from spm.__wrapper__ import Runtime


def spm_dcm_fmri_mode(*args, **kwargs):
  """  Generate modes and matrices for spectral DCM from Lyapunov exponents  
    FORMAT [U,E,F] = spm_dcm_fmri_mode(Ev,modes)  
    Ev    - (log of negative) Lyapunov exponents or eigenvalues of Jacobian  
    modes - modes or eigenvectors  
     
    U     - weighted modes; such that U*U' = F  
    E     - (neuronal) effective  connectivity matrix  
    F     - (neuronal) functional connectivity matrix E = -inv(F)/2  
     
    This routine computes the connecivity graph for spectral DCM (modes).  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_dcm_fmri_mode.m)
  """

  return Runtime.call("spm_dcm_fmri_mode", *args, **kwargs)
