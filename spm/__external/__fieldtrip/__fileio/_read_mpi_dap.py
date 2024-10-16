from spm.__wrapper__ import Runtime


def _read_mpi_dap(*args, **kwargs):
  """  READ_MPI_DAP read the analog channels from a DAP file  
    and returns the values in microvolt (uV)  
     
    Use as  
      [dap] = read_mpi_dap(filename)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_mpi_dap.m)
  """

  return Runtime.call("read_mpi_dap", *args, **kwargs)
