from spm.__wrap__ import _Runtime


def mci_lds_par2lat(*args, **kwargs):
  """  Convert parmas to latent params  
    FORMAT [P] = mci_lds_par2lat (Pt,M)  
     
    Pt    params   
    M     model struct  
     
    P     params (latent)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/lds/mci_lds_par2lat.m)
  """

  return _Runtime.call("mci_lds_par2lat", *args, **kwargs)
