from spm._runtime import Runtime


def spm_logo(*args, **kwargs):
    r"""
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
          S.save    - If true, generates image files for re-use  
         
        h           - Handle figure  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_logo.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_logo", *args, **kwargs)
