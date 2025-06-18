from mpython import Runtime


def fiff_write_epochs(*args, **kwargs):
    """

        function fiff_write_epochs(name,data)

        name     filename
        data     the data structure returned from fiff_write_evoked


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_write_epochs.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_epochs", *args, **kwargs, nargout=0)
