from spm._runtime import Runtime


def spm_lx_phase(*args, **kwargs):
    """
      Observation function for phase-coupled oscillators  
        FORMAT [G] = spm_lx_phase(P,M)  
         
        G     Observations y = Gx  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_lx_phase.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_lx_phase", *args, **kwargs)
