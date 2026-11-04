from spm._runtime import Runtime


def fil_prune(*args, **kwargs):
    r"""
      Prune the model  
        FORMAT model = fil_prune(model,sett,p)  
        model - The learned model from fil_train  
         
        Take a fitted model, orthogonalise and remove irrelevent latent  
        variables.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MB/fil_prune.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fil_prune", *args, **kwargs)
