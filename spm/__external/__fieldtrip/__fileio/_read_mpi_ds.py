from spm._runtime import Runtime


def _read_mpi_ds(*args, **kwargs):
    r"""
      READ_MPI_DS reads all DAP files from a directory containing files or  
        alternatively a single DAP file and returns it in a simplified FieldTrip  
        format. The analog channels and spike channels are both returned in a  
        continuous format.  
         
        Use as  
          [hdr, dat] = read_mpi_ds(dirname)  
        or  
          [hdr, dat] = read_mpi_ds(filename)  
         
        See also READ_MPI_DAP  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_mpi_ds.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_mpi_ds", *args, **kwargs)
