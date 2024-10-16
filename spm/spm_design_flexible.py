from spm.__wrapper__ import Runtime


def spm_design_flexible(*args, **kwargs):
  """  Create H partition of design matrix  
    FORMAT [H,Hnames,B,Bnames] = spm_design_flexible(fblock,I)  
     
    fblock   - Part of job structure containing within-subject design info  
    I        - Nscan x 4 factor matrix  
     
    H        - Component of design matrix describing conditions  
    Hnames   - Condition names  
    B        - Component of design matrix describing blocks  
    Bnames   - Block names  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_design_flexible.m)
  """

  return Runtime.call("spm_design_flexible", *args, **kwargs)
