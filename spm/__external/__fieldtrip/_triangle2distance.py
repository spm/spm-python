from spm.__wrapper__ import Runtime


def _triangle2distance(*args, **kwargs):
    """
      TRIANGLE2DISTANCE computes the geodesic distance (across the edges) on a  
        mesh, using Dijkstra's algorithm. The Dijkstra code is an efficient  
        vectorized version of a function from MIT's graphtool toolbox, operating  
        on an adjacency matrix.  
         
        Use as  
          d = triangle2distance(tri, pos, s)  
         
        Input arguments:  
          tri = Mx3 matrix describing the triangles  
          pos = Nx3 matrix describing the position of the vertices  
          s   = (can be empty), scalar or vector with indices for the points for  
                which the distance (to all other points) will be computed. If  
                empty or not defined, all points will be considered.  
         
        Output argument:  
          d   = Nxnumel(s) distance matrix  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/triangle2distance.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("triangle2distance", *args, **kwargs)
