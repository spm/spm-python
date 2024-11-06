from spm.__wrapper__ import Runtime


def _getorthoviewpos(*args, **kwargs):
    """
      GETORTHOVIEWPOS obtains the orthographic projections of 3D positions  
        based on a given coordinate system and viewpoint  
         
        Use as  
          getorthoviewpos(pos, coordsys, viewpoint)  
         
        For example  
          getorthoviewpoint(pos, 'mni', 'superior')  
         
        See alo SETVIEWPOINT, COORDSYS2LABEL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/getorthoviewpos.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("getorthoviewpos", *args, **kwargs)
