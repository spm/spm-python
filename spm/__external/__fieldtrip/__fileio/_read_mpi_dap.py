from spm._runtime import Runtime


def _read_mpi_dap(*args, **kwargs):
    r"""
      READ_MPI_DAP read the analog channels from a DAP file  
        and returns the values in microvolt (uV)  
         
        Use as  
          [dap] = read_mpi_dap(filename)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_mpi_dap.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_mpi_dap", *args, **kwargs)
