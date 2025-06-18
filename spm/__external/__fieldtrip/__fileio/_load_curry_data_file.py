from mpython import Runtime


def _load_curry_data_file(*args, **kwargs):
    """
    load_curry_data_file is a function.
          [orig, data] = load_curry_data_file(datafile)


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/load_curry_data_file.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("load_curry_data_file", *args, **kwargs)
