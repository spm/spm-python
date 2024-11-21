from spm.__wrapper__ import Runtime


def spm_DEM_generate(*args, **kwargs):
    """
      Generate data for a Hierarchical Dynamic Model (HDM)  
        FORMAT [DEM] = spm_DEM_generate(M,N,P,h,g): N-samples using z  
        FORMAT [DEM] = spm_DEM_generate(M,U,P,h,g): size(U,2) samples using U  
         
        M(i)     - HDM  
        U(n x N} - causes or N number of causes  
        P{i}     - model-parameters for level i (defaults to M.pE)  
        h{i}     - log-precisions   for level i (defaults to 32 - no noise)  
        g{i}     - log-precisions   for level i (defaults to 32 - no noise)  
         
        generates  
        DEM.M    - hierarchical model (checked)  
        DEM.Y    - responses or data  
         
        and true causes NB: v{end} = U or z{end} (last level innovations)  
        DEM.pU.v   
        DEM.pU.x  
        DEM.pU.e  
        DEM.pP.P  
        DEM.pH.h  
         
        NB: [lower bound on] random fluctuations will default to unit variance if  
        not specified in M(i).V and M(i).W  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_DEM_generate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_DEM_generate", *args, **kwargs)
