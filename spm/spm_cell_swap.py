from spm.__wrapper__ import Runtime


def spm_cell_swap(*args, **kwargs):
  """  Swap columns for cells in matrix arrays  
    FORMAT y = spm_cell_swap(x)  
    y{:,i}(:,j) = x{:,j}(:,i);  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_cell_swap.m)
  """

  return Runtime.call("spm_cell_swap", *args, **kwargs)
