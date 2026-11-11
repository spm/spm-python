from spm._runtime import Runtime


def _setviewpoint(*args, **kwargs):
    r"""
      SETVIEWPOINT changes the viewpoint for a 3D image that contains data in a known coordinate system  
         
        Use as  
          setviewpoint(ax, coordsys, viewpoint)  
         
        For example  
          setviewpoint(gca, 'mni', 'left')  
         
        See also GETORTHOVIEWPOS, COORDSYS2LABEL  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/setviewpoint.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("setviewpoint", *args, **kwargs, nargout=0)
