from spm._runtime import Runtime


def DEM_demo_MMN_gen(*args, **kwargs):
    r"""
      generates hidden states for a MMN roving paradigm using spm_DEM  
        FORMAT [x,DEM] = DEM_demo_MMN_gen(P,G,U);  
         
        P   - parameters  
        G   - generative (response) model  
        U   - design  
         
        x   - hidden neuronal states {(ns x (nr x 8)}; ... }  
        DEM - stucture array of DEM structures  
         
        see DEM_demo_MMN  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_demo_MMN_gen.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_demo_MMN_gen", *args, **kwargs)
