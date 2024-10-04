from spm.__wrap__ import _Runtime


def mci_lds_group_data(*args, **kwargs):
  """  Generate LDS data for a group of subjects  
    FORMAT [pinit,pflow,names,M,U,Y] = mci_lds_group_data (lds)  
     
    lds        Data structure with fields:  
     
    .R         R.pE, R.pC prior over initial conds  
    .sd        Standard deviation of observation noise  
    .Nsub      Number of subjects  
    .Nobs      Number of observations per subject  
    .model     'lds_real','forward',etc.  
    .flow_par  'fixed' or 'random'  
    .init_par  'fixed' or 'random'  
      
    pinit      Initial params  
    pflow      Flow params  
    names      names of parameters  
    M          Cell of models  
    U          Cell of inputs  
    Y          Cell of data  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/lds/mci_lds_group_data.m)
  """

  return _Runtime.call("mci_lds_group_data", *args, **kwargs)
