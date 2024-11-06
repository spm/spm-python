from spm.__wrapper__ import Runtime


def _triangle4pt(*args, **kwargs):
    """
      TRIANGLE4PNT takes the volume model and estimates the 4th point of each  
        triangle of each mesh.  
         
        Use as  
          headmodel = triangle4pt(headmodel)  
         
        In each headmodel.bnd sub-structure, a field '.pnt4' is added. The '.pnt4'  
        field is a Ntri*3 matrix, with the coordinates of a point for each  
        triangle in the meshed surface.  
         
        Explanations:  
        The point is that for some BEM, specifically 'solid angle', calculation  
        it is necessary to estimate the local curvature of the true surface which  
        is approximated by the flat triangle. One way to proceed is to use  
        "close by" vertices to estimate the overall area's curvature.  
        A more elegant(?) way uses a 4th point for each triangle: the "centroid"  
        of the triangle is simply pusehd away from the triangle surface to fix  
        the local surface curvature (assuming the surface is smooth enough).  
        This 4th point is thus hovering above/under the triangle and can be used  
        to fit a sphere on the triangle in a realistic way.  
         
        Method:  
        - The 4th point can/could be defined at the tessalation stage, based on  
          the anatomical images directly.  
        - With any model, the curvature can be estimated/approximated by looking  
          at the vertices around the triangle considered and fit a sphere on  
          those few vertices, assuming the surface is smooth enough  
        The latter option is the one followed here.  
        The extra-vertices considered here are those 3 which are linked to the  
        triangle by 2 edges.  
       __________________________________________________________________________  
         
        written by Christophe Phillips, 2009/01/19  
        Cyclotron Research Centre, University of li?ge, belgium  
         
        $Id$  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/triangle4pt.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("triangle4pt", *args, **kwargs)
