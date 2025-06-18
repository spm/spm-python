from mpython import Runtime


def _val2nearestchan(*args, **kwargs):
    """
      VAL2NEARESTCHAN returns the label of the channel with the value nearest
        to the specified value.

        use as channame = val2nearestchan(data,val)
        val = [time y] with time in sec
        works only on raw data


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/val2nearestchan.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("val2nearestchan", *args, **kwargs)
