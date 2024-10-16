from spm.__wrapper__ import Runtime


def spm_dcm_csd_source_plot(*args, **kwargs):
  """  Spectral response (G) of a single source neural mass model  
    FORMAT [G] = spm_dcm_csd_source_plot(model,s)  
     
    model - 'ERP', 'SEP', 'CMC', 'LFP', 'NMM' or 'MFM'  
    s     - indices of hidden neuronal states to plot  
    P     - parameters  
    N     - twice the maximum frequency  
     
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_csd_source_plot.m)
  """

  return Runtime.call("spm_dcm_csd_source_plot", *args, **kwargs)
