from spm.__wrapper__ import Runtime


def _intersect_line(*args, **kwargs):
    """
      INTERSECT_LINE finds the intersection points between a mesh and a line.  
         
        Use as:  
          [points, pos, indx] = intersect_line(pnt, tri, pnt1, pnt2)  
          
        Where pnt (Nx3) and tri (Mx3) define the mesh, and pnt1 (1x3) and pnt2  
        (1x3) define the line. The output argument points (Px3) are the  
        intersection points, pos (Px1) the location on the line (relative to  
        pnt1) and indx is the index to the triangles of the mesh that are  
        intersected.  
         
        This code is based from a function from the geom3d toolbox, that can be  
        found on matlab's file exchange. The original help is pasted below. The  
        original function was released under the BSD-license.  
         
        Adapted to FieldTrip by Jan-Mathijs Schoffelen 2012  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/intersect_line.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("intersect_line", *args, **kwargs)
