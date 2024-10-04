from spm.__wrap__ import _Runtime


def _reorderdim(*args, **kwargs):
  """  REORDERDIM reorders array A along dimension dim with the specified  
    indices inds. The following should output 1:  
     
      B1 = reorderdim(A,2,[1 3 2]);  
      B2 = A(:,[1 3 2],:,:);  
     
      all(B1(:) == B2(:))  
     
    The main use for this function is when a selection as displayed above  
    needs to be made when the number of dimensions of A is only known at  
    runtime and not at 'code'-time (i.e. when A can have arbitrary  
    dimensions).  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/reorderdim.m)
  """

  return _Runtime.call("reorderdim", *args, **kwargs)
