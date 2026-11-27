from spm._runtime import Runtime


def spm_voice_i(*args, **kwargs):
    r"""
      Get indices, word strings or priors from lexicon  
        FORMAT [str] = spm_voice_i(i)  
        FORMAT [i  ] = spm_voice_i(str)  
        FORMAT [i,P] = spm_voice_i(str)  
         
        str  - string or cell array  
        i    - index in lexicon (VOX.LEX)  
        P    - corresponding array of prior probabilities  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_voice_i.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_voice_i", *args, **kwargs)
