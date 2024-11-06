from spm.__wrapper__ import Runtime


def _elproj(*args, **kwargs):
    """
      ELPROJ makes a azimuthal projection of a 3D electrode cloud  
         on a plane tangent to the sphere fitted through the electrodes  
         the projection is along the z-axis  
         
         [proj] = elproj([x, y, z], 'method');  
         
        Method should be one of these:  
            'gnomic'  
            'stereographic'  
            'orthographic'  
            'inverse'  
            'polar'  
         
        Imagine a plane being placed against (tangent to) a globe. If  
        a light source inside the globe projects the graticule onto  
        the plane the result would be a planar, or azimuthal, map  
        projection. If the imaginary light is inside the globe a Gnomonic  
        projection results, if the light is antipodal a Sterographic,  
        and if at infinity, an Orthographic.  
         
        The default projection is a polar projection (BESA like).  
        An inverse projection is the opposite of the default polar projection.  
         
        See also PROJECTTRI  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/elproj.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("elproj", *args, **kwargs)
