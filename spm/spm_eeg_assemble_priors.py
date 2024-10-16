from spm.__wrapper__ import Runtime


def spm_eeg_assemble_priors(*args, **kwargs):
  """  Predict sensor level impact of sources in Qp given sensor noise Qe  
    FORMAT [LCpL,Q,sumLCpL,QE,Cy,M,Cp,Cq,Lq] = spm_eeg_assemble_priors(L,Qp,Qe,ploton,h)  
    L       - lead fields  
    Qp      - priors on source level dipole moment nAm/(mm2) per sample  
    Qe      - sensor level variance in fT^2 per sample  
    h       - optional hyperparameters that scale the variance components in  
              Qe and Qp (assume sensor followed by source level parameters)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_assemble_priors.m)
  """

  return Runtime.call("spm_eeg_assemble_priors", *args, **kwargs)
