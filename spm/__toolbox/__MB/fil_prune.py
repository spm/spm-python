from spm.__wrapper__ import Runtime


def fil_prune(*args, **kwargs):
    """
      Prune the model  
        FORMAT model = fil_prune(model,sett,p)  
        model - The learned model from fil_train  
         
        Take a fitted model, orthogonalise and remove irrelevent latent  
        variables.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MB/fil_prune.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fil_prune", *args, **kwargs)
