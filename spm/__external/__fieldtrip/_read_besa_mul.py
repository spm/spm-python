from mpython import Runtime


def _read_besa_mul(*args, **kwargs):
    """
      READ_BESA_MUL reads data from a BESA multiplexed (*.mul) file

        Use as
          dat = read_besa_mul(filename);


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/read_besa_mul.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_besa_mul", *args, **kwargs)
