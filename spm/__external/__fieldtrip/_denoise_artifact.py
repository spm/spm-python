from spm.__wrapper__ import Runtime


def _denoise_artifact(*args, **kwargs):
    """
      DENOISE_ARTIFACT can be used for denoising source separation (DSS)  
        during component analysis  
         
        See also COMPONENTANALYSIS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/denoise_artifact.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("denoise_artifact", *args, **kwargs)
