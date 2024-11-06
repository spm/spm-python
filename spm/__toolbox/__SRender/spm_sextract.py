from spm.__wrapper__ import Runtime


def spm_sextract(*args, **kwargs):
    """
      Surface extraction  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/SRender/spm_sextract.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_sextract", *args, **kwargs)
