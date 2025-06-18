from mpython import Runtime


def _avgref(*args, **kwargs):
    """
      AVGREF computes the average reference in each column
          [data] = avgref(data)

        or it computes the re-referenced data relative to the
        average over the selected channels
          [data] = avgref(data, sel)


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/private/avgref.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("avgref", *args, **kwargs)
