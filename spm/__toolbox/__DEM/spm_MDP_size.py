from spm.__wrapper__ import Runtime


def spm_MDP_size(*args, **kwargs):
    """
      Dimensions of MDP  
        FORMAT [Nf,Ns,Nu,Ng,No] = spm_MDP_size(mdp)  
        Nf  - number of factors  
        Ns  - states per factor  
        Nu  - control per factors  
        Ng  - number of modalities  
        No  - levels per modality  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_size.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MDP_size", *args, **kwargs)
