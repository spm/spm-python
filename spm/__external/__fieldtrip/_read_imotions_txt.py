from mpython import Runtime


def _read_imotions_txt(*args, **kwargs):
    """
      READ_IMOTIONS_TXT reads *.txt files that are exported from the iMotions software.

        Use as
          dat = read_imotions_txt(filename

        See also TEXTSCAN


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/read_imotions_txt.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_imotions_txt", *args, **kwargs)
