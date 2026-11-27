from spm._runtime import Runtime


def _threadblocks(*args, **kwargs):
    r"""
      Set the size of a block of threads and grid on a CUDA kernel  
        FORMAT kernel = threadblocks(kernel,d)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Spatial/private/threadblocks.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("threadblocks", *args, **kwargs)
