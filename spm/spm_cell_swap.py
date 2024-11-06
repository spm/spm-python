from spm.__wrapper__ import Runtime


def spm_cell_swap(*args, **kwargs):
    """
      Swap columns for cells in matrix arrays  
        FORMAT y = spm_cell_swap(x)  
        y{:,i}(:,j) = x{:,j}(:,i);  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_cell_swap.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cell_swap", *args, **kwargs)
