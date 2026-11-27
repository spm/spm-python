from spm._runtime import Runtime


def _read_yorkinstruments_hdf5_meta(*args, **kwargs):
    r"""
      READ_YPRKINSTRUMENTS_HDF5_META reads the metatada and header information from a .meghdf5 file  
         
        Use as  
          info=read_yorkinstruments_hdf5_meta(datafile)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_yorkinstruments_hdf5_meta.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_yorkinstruments_hdf5_meta", *args, **kwargs)
