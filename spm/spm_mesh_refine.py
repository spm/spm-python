from spm.__wrapper__ import Runtime


def spm_mesh_refine(*args, **kwargs):
  """  Refine a triangle mesh  
    FORMAT M = spm_mesh_refine(M)  
    M        - a patch structure or gifti object  
   __________________________________________________________________________  
     
    See also:  
     
    R.E. Bank, A.H. Sherman and A. Weiser. Refinement Algorithms and Data   
    Structures for Regular Local Mesh Refinement. Scientific Computing   
    (Applications of Mathematics and Computing to the Physical Sciences)  
    (R. S. Stepleman, ed.), North-Holland (1983), 3-17.  
    https://ccom.ucsd.edu/~reb/reports/a23.pdf.gz  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mesh_refine.m)
  """

  return Runtime.call("spm_mesh_refine", *args, **kwargs)
