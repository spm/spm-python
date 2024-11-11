from spm.__wrapper__ import Runtime


def spm_mci_mh_update(*args, **kwargs):
    """
      Update parameters using Metropolis-Hastings  
        FORMAT [next,accepted,bayes_fb,dL] = spm_mci_mh_update (curr,prop,verbose)  
         
        curr      quantities re current state  
        prop      quantities re proposed state  
        verbose   1 for text output  
         
        next      next state  
        accepted  1 for accepted proposal  
        bayes_fb  Log Bayes factor for forward versus backward transition  
        dL        Proposed difference in log joint  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_mh_update.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_mh_update", *args, **kwargs)
