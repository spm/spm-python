from spm.__wrapper__ import Runtime


def spm_SEM_gen_full(*args, **kwargs):
    """
      Slow/saccadic eye movement prediction scheme - for model  
        FORMAT [y,DEM] = spm_SEM_gen_full(P,M,U)  
         
          P - parameters  
          M - (meta) model structure  
          U - trial-specific parameter deviates  
         
          y   - {[ns,nx];...} - predictions for nx states {trials}  
                              - for ns samples (normalised lag)  
         
        This generative routine is the same as spm_SEM_gen but includes an extra  
        hierarchical level to infer the phase of underlying target motion. this  
        sort of generative model is required when characterising violation or  
        omission responses due to departures from the expected trajectory.  
         
        see also: spm_SEM_gen  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/SPEM_and_DCM/spm_SEM_gen_full.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_SEM_gen_full", *args, **kwargs)
