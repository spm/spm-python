from spm.__wrapper__ import Runtime


def spm_mb_output(*args, **kwargs):
    """
      Write output from groupwise normalisation and segmentation of images  
        FORMAT res = spm_mb_output(cfg)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MB/spm_mb_output.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mb_output", *args, **kwargs)
