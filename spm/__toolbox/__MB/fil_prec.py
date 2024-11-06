from spm.__wrapper__ import Runtime


def fil_prec(*args, **kwargs):
    """
      Attach matrices for computing priors  
        FORMAT model = fil_prec(model,sett)  
        model - The learned model from fil_train  
        sett  - Settings  
                Uses sett.matname, sett.nu and sett.v0  
         
        Takes a fitted model, and converts to a form that allows the  
        distributions of latent variables to be estimated by a neural network  
        type formulation.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MB/fil_prec.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fil_prec", *args, **kwargs)
