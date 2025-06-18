from mpython import Runtime


def _setviewpoint(*args, **kwargs):
    """
      SETVIEWPOINT changes the viewpoint for a 3D image that contains data in a known coordinate system

        Use as
          setviewpoint(ax, coordsys, viewpoint)

        For example
          setviewpoint(gca, 'mni', 'left')

        See also GETORTHOVIEWPOS, COORDSYS2LABEL


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/setviewpoint.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("setviewpoint", *args, **kwargs, nargout=0)
