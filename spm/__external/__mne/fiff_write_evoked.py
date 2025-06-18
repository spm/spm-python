from mpython import Runtime


def fiff_write_evoked(*args, **kwargs):
    """

        function fiff_write_evoked(name,data,datatype)

        name     filename
        data     the data structure returned from fiff_read_evoked


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_write_evoked.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_evoked", *args, **kwargs, nargout=0)
