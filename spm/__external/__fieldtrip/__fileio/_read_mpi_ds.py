from spm.__wrapper__ import Runtime


def _read_mpi_ds(*args, **kwargs):
    """
      READ_MPI_DS reads all DAP files from a directory containing files or  
        alternatively a single DAP file and returns it in a simplified FieldTrip  
        format. The analog channels and spike channels are both returned in a  
        continuous format.  
         
        Use as  
          [hdr, dat] = read_mpi_ds(dirname)  
        or  
          [hdr, dat] = read_mpi_ds(filename)  
         
        See also READ_MPI_DAP  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_mpi_ds.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_mpi_ds", *args, **kwargs)
