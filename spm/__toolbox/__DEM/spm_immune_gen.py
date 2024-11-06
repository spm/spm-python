from spm.__wrapper__ import Runtime


def spm_immune_gen(*args, **kwargs):
    """
      Generative model of an immune response  
        FORMAT [Y,X] = spm_immune_gen(P,M,U)  
        Y   - timeseries data  
        X   - latent states  
        P   - Priors  
        M   - Model  
        U   - inputs (timing of measurements)  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_immune_gen.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_immune_gen", *args, **kwargs)
