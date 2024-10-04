from spm.__wrap__ import _Runtime


def mci_lds_plot_params(*args, **kwargs):
  """  Plot results of group LDS estimation  
    FORMAT [rmse] = mci_lds_plot_results (MCI,lds)  
     
    MCI      MCI-MFX data structure  
    lds      true model data structure with fields:  
     
    .pinit    true init params  
    .pflow    true flow params  
     
    rmse      root mean square errors  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/lds/mci_lds_plot_params.m)
  """

  return _Runtime.call("mci_lds_plot_results", *args, **kwargs)
