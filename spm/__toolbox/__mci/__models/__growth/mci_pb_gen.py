from mpython import Runtime


def mci_pb_gen(*args, **kwargs):
    """
      Preece-Baines growth model
        FORMAT [y] = mci_pb_gen (P,M,U)

        P         parameters
        M         model
        U         inputs

        y         time series
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/growth/mci_pb_gen.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_pb_gen", *args, **kwargs)
