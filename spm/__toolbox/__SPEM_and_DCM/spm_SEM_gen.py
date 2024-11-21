from spm.__wrapper__ import Runtime


def spm_SEM_gen(*args, **kwargs):
    """
      Slow/saccadic eye movement prediction scheme  
        FORMAT [y,DEM] = spm_SEM_gen(P,M,U)  
         
          P - parameters  
          M - (meta) model structure  
          U - trial-specific parameter deviates  
         
          y - {[ns,nx];...} - predictions for nx states {trials}  
                            - for ns samples (normalised lag)  
         
        This smooth pursuit eye movement routine generates one cycle of motion  
        under prior beliefs about a sinusoidal trajectory with variable phase.  
         
        see also: spm_SEM_gen_full  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/SPEM_and_DCM/spm_SEM_gen.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_SEM_gen", *args, **kwargs)
