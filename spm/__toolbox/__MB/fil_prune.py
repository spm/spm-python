from spm.__wrapper__ import Runtime


def fil_prune(*args, **kwargs):
  """  Prune the model  
    FORMAT model = fil_prune(model,sett,p)  
    model - The learned model from fil_train  
     
    Take a fitted model, orthogonalise and remove irrelevent latent  
    variables.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MB/fil_prune.m)
  """

  return Runtime.call("fil_prune", *args, **kwargs)
