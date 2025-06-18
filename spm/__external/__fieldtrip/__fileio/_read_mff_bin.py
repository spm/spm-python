from mpython import Runtime


def _read_mff_bin(*args, **kwargs):
    """
      READ_MFF_BIN

        Use as
          [hdr] = read_mff_bin(filename)
        or
          [dat] = read_mff_bin(filename, begblock, endblock);


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_mff_bin.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_mff_bin", *args, **kwargs)
