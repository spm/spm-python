from mpython import Runtime


def _translate(*args, **kwargs):
    """
      TRANSLATE returns the homogenous coordinate transformation matrix
        corresponding to a translation along the x, y and z-axis

        Use as
          [H] = translate(T)
        where
          T   [tx, ty, tz] translation along each of the axes
          H   corresponding homogenous transformation matrix

        See also ROTATE, SCALE, RIGIDBODY, QUATERNION, HOMOGENOUS2TRADITIONAL


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/private/translate.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("translate", *args, **kwargs)
