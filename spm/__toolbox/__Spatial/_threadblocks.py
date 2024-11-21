from spm.__wrapper__ import Runtime


def _threadblocks(*args, **kwargs):
    """
      Set the size of a block of threads and grid on a CUDA kernel  
        FORMAT kernel = threadblocks(kernel,d)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/private/threadblocks.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("threadblocks", *args, **kwargs)
