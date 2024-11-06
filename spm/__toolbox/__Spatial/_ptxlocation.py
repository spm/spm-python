from spm.__wrapper__ import Runtime


def _ptxlocation(*args, **kwargs):
    """
      Location of a PTX file used in GPU computations  
        FORMAT ptx = ptxlocation(nam)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/private/ptxlocation.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ptxlocation", *args, **kwargs)
