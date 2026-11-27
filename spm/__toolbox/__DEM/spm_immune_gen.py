from spm._runtime import Runtime


def spm_immune_gen(*args, **kwargs):
    r"""
      Generative model of an immune response  
        FORMAT [Y,X] = spm_immune_gen(P,M,U)  
        Y   - timeseries data  
        X   - latent states  
        P   - Priors  
        M   - Model  
        U   - inputs (timing of measurements)  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_immune_gen.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_immune_gen", *args, **kwargs)
