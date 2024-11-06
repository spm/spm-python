from spm.__wrapper__ import Runtime


def _mesh_laplacian(*args, **kwargs):
    """
      MESH_LAPLACIAN: Laplacian of irregular triangular mesh  
         
        Useage: [lap,edge] = mesh_laplacian(vertex,face)  
         
        Returns 'lap', the Laplacian (2nd spatial derivative) of an  
        irregular triangular mesh, and 'edge', the linear distances  
        between vertices of 'face'.  'lap' and 'edge' are square,  
        [Nvertices,Nvertices] in size, sparse in nature.  
         
        It is assumed that 'vertex' contains the (x,y,z) Cartesian  
        coordinates of each vertex and that 'face' contains the  
        triangulation of vertex with indices into 'vertex' that  
        are numbered from 1:Nvertices.  For information about  
        triangulation, see 'help convhull' or 'help convhulln'.  
         
        The neighbouring vertices of vertex 'i' is given by:  
         
        k = find(edge(i,:));  
         
        The math of this routine is given by:  
         
        Oostendorp, Oosterom & Huiskamp (1989),  
        Interpolation on a triangulated 3D surface.  
        Journal of Computational Physics, 80: 331-343.  
         
        See also, eeg_interp_scalp_mesh  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/private/mesh_laplacian.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mesh_laplacian", *args, **kwargs)
