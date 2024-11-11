from spm.__wrapper__ import Runtime


def _mesh_sphere(*args, **kwargs):
    """
      MESH_SPHERE creates spherical mesh, with approximately nvertices vertices  
         
        Use as  
          [pos, tri] = mesh_sphere(n, method)  
         
        The input parameter 'n' specifies the (approximate) number of vertices. If n is  
        empty, or undefined, a 12 vertex icosahedron will be returned. If n is specified  
        but the method is not specified, the most optimal method will be selected based on  
        n.  
        - If log4((n-2)/10) is an integer, the mesh will be based on an icosahedron.  
        - If log4((n-2)/4) is an integer, the mesh will be based on a refined octahedron.  
        - If log4((n-2)/2) is an integer, the mesh will be based on a refined tetrahedron.  
        - Otherwise, an msphere will be used.  
         
        The input parameter 'method' defines which algorithm or approach to use. This can  
        be 'icosahedron', 'octahedron', 'tetrahedron', 'fibonachi', 'msphere', or 'ksphere'.  
         
        See also MESH_TETRAHEDRON, MESH_OCTAHEDRON, MESH_ICOSAHEDRON  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/mesh_sphere.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mesh_sphere", *args, **kwargs)
