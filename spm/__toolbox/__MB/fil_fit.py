from spm.__wrapper__ import Runtime


def fil_fit(*args, **kwargs):
    """
      Bohning bound CCA stuff  
        FORMAT [mod,Z,V] = fil_fit(F,sett,ind,p,mod,Z,Z0,P0)  
        F{l}      - Nvox x M x N  
        ind       - N x L  
        p         - N x 1  
        mod(l).mu - Nvox x M  
        mod(l).W  - Nvox x M x K  
        Z         - K x N  
        Z0        - K x N  
        P0        - K x K  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MB/fil_fit.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fil_fit", *args, **kwargs)
