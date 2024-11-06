from spm.__wrapper__ import Runtime


def _read_yorkinstruments_hdf5_meta(*args, **kwargs):
    """
      READ_YPRKINSTRUMENTS_HDF5_META reads the metatada and header information from a .meghdf5 file  
         
        Use as  
          info=read_yorkinstruments_hdf5_meta(datafile)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_yorkinstruments_hdf5_meta.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_yorkinstruments_hdf5_meta", *args, **kwargs)
