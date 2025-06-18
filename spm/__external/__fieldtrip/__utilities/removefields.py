from mpython import Runtime


def removefields(*args, **kwargs):
    """
      REMOVEFIELDS makes a selection of the fields in a structure

        Use as
          s = removefields(s, fields);

        See also KEEPFIELDS, COPYFIELDS


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/removefields.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("removefields", *args, **kwargs)
