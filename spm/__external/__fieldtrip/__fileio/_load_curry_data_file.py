from spm._runtime import Runtime


def _load_curry_data_file(*args, **kwargs):
    r"""
    load_curry_data_file is a function.  
          [orig, data] = load_curry_data_file(datafile)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/load_curry_data_file.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("load_curry_data_file", *args, **kwargs)
