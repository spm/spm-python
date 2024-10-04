from spm.__wrap__ import _Runtime


def spm_mci_vw_init(*args, **kwargs):
  """  Initialise fixed and random effects  
    FORMAT [w_init,v_init,assign,update_ffx,update_rfx] = spm_mci_vw_init (MCI)  
     
    MCI       MCI data structure  
     
    w_init        initial rfx values  
    v_init        initial ffx values  
    assign        data structure describing how rfx/ffx are assigned   
                  to initial conditions, flow and output params  
    update_ffx    (1/0)  
    update_rfx    (1/0)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_vw_init.m)
  """

  return _Runtime.call("spm_mci_vw_init", *args, **kwargs)
