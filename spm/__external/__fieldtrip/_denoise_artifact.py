from spm._runtime import Runtime


def _denoise_artifact(*args, **kwargs):
    r"""
      DENOISE_ARTIFACT can be used for denoising source separation (DSS)  
        during component analysis  
         
        See also COMPONENTANALYSIS  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/denoise_artifact.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("denoise_artifact", *args, **kwargs)
