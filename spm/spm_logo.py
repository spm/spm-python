from mpython import Runtime


def spm_logo(*args, **kwargs):
    """
      Generate SPM's new logo
        FORMAT h = spm_logo(S)

        S           - input structure
         Optional fields of S:
          S.ver     - Set the version number, defaults to current SPM version
          S.altm    - Which style of M to use? False for M and True for m.
          S.width   - 2x1 array to set widths of the text of logo.
          S.colour  - Text colour
          S.background    - background colour
          S.angle   - Angle (in degrees) of the isometric progection

        h           - Handle figure
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_logo.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_logo", *args, **kwargs)
