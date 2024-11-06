from spm.__wrapper__ import Runtime


def DEM_demo_MMN_gen(*args, **kwargs):
    """
      generates hidden states for a MMN roving paradigm using spm_DEM  
        FORMAT [x,DEM] = DEM_demo_MMN_gen(P,G,U);  
         
        P   - parameters  
        G   - generative (response) model  
        U   - design  
         
        x   - hidden neuronal states {(ns x (nr x 8)}; ... }  
        DEM - stucture array of DEM structures  
         
        see DEM_demo_MMN  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_MMN_gen.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_MMN_gen", *args, **kwargs)
