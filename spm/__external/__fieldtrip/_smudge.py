from spm.__wrapper__ import Runtime


def _smudge(*args, **kwargs):
    """
      SMUDGE(DATIN, TRI) computes a smudged version of the input data datain,  
        given a triangulation tri. The algorithm is according to what is in  
        MNE-Suite, documented in chapter 8.3  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/smudge.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("smudge", *args, **kwargs)
