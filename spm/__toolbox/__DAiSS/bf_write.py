from spm.__wrapper__ import Runtime


def bf_write(*args, **kwargs):
    """
      Write out the results of beamforming analysis  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_write.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_write", *args, **kwargs)
