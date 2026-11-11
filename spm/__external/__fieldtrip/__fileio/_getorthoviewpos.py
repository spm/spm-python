from spm._runtime import Runtime


def _getorthoviewpos(*args, **kwargs):
    r"""
      GETORTHOVIEWPOS obtains the orthographic projections of 3D positions  
        based on a given coordinate system and viewpoint  
         
        Use as  
          getorthoviewpos(pos, coordsys, viewpoint)  
         
        For example  
          getorthoviewpoint(pos, 'mni', 'superior')  
         
        See alo SETVIEWPOINT, COORDSYS2LABEL  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/getorthoviewpos.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("getorthoviewpos", *args, **kwargs)
