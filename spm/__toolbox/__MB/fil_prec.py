from spm.__wrap__ import _Runtime


def fil_prec(*args, **kwargs):
  """  Attach matrices for computing priors  
    FORMAT model = fil_prec(model,sett)  
    model - The learned model from fil_train  
    sett  - Settings  
            Uses sett.matname, sett.nu and sett.v0  
     
    Takes a fitted model, and converts to a form that allows the  
    distributions of latent variables to be estimated by a neural network  
    type formulation.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MB/fil_prec.m)
  """

  return _Runtime.call("fil_prec", *args, **kwargs)
