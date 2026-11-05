from spm._runtime import Runtime


def spm_cell_swap(*args, **kwargs):
    r"""
      Swap columns for cells in matrix arrays  
        FORMAT y = spm_cell_swap(x)  
        y{:,i}(:,j) = x{:,j}(:,i);  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_cell_swap.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cell_swap", *args, **kwargs)
