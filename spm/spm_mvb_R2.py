from spm.__wrapper__ import Runtime


def spm_mvb_R2(*args, **kwargs):
    """
      Return the proportion of variance explained by the (MVB) MAP estimates  
        FORMAT [R2,X,P] = spm_mvb_R2(MVB)  
         
        MVB - MVB structure  
        R2  - proportion of variance explained  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mvb_R2.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mvb_R2", *args, **kwargs)
