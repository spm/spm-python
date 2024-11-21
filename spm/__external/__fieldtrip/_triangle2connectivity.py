from spm.__wrapper__ import Runtime


def _triangle2connectivity(*args, **kwargs):
    """
      TRIANGLE2CONNECTIVITY computes a connectivity-matrix from a triangulation.  
         
        Use as  
         [connmat] = triangle2connectivity(tri)  
        or  
         [connmat] = triangle2connectivity(tri, pos)  
         
        The input tri is an Mx3 matrix describing a triangulated surface,  
        containing indices to connecting vertices. The output connmat is a sparse  
        logical NxN matrix, with ones, where vertices are connected, and zeros  
        otherwise.  
         
        If you specify the vertex positions in the second input argument as Nx3  
        matrix, the output will be a sparse matrix with the lengths of the  
        edges between the connected vertices.  
         
        See also CHANNELCONNECTIVIY  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/triangle2connectivity.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("triangle2connectivity", *args, **kwargs)
