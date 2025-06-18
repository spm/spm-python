from mpython import Runtime


def _globalrescale(*args, **kwargs):
    """
      GLOBALRESCALE creates the homogenous spatial transformation matrix
        for a 7 parameter rigid-body transformation with global rescaling

        Use as
          [H] = globalrescale(f)

        The transformation vector f should contain the
          x-shift
          y-shift
          z-shift
        followed by the
          pitch (rotation around x-axis)
          roll  (rotation around y-axis)
          yaw   (rotation around z-axis)
        followed by the
          global rescaling factor


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/globalrescale.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("globalrescale", *args, **kwargs)
