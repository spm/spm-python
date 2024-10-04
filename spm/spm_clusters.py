from spm.__wrap__ import _Runtime


def spm_clusters(*args, **kwargs):
  """  Return the cluster index for a point list  
    FORMAT A = spm_clusters(L,n)  
    L     - locations [x y x]' {in voxels} ([3 x m] matrix)  
    n     - connectivity criterion (see spm_bwlabel) [Default: 18]  
     
    A     - cluster index or region number ([1 x m] vector)  
   __________________________________________________________________________  
     
    spm_clusters characterises a point list of voxel values defined with  
    their locations (L) in terms of edge, face and vertex connected  
    subsets, returning a list of indices in A, such that the ith location  
    belongs to cluster A(i) (using an 18 connectivity scheme).  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_clusters.m)
  """

  return _Runtime.call("spm_clusters", *args, **kwargs)
