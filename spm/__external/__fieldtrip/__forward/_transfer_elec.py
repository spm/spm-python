from spm.__wrapper__ import Runtime


def _transfer_elec(*args, **kwargs):
  """  TRANSFER_ELEC is the transfermatrix from vertex to electrode potentials  
    using bi-linear interpolation over the triangles  
     
    tra = transfer_elec(pnt, tri, el)  
     
    the Nx3 matrix el shold contain [tri, la, mu] for each electrode  
     
    See also PROJECT_ELEC  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/transfer_elec.m)
  """

  return Runtime.call("transfer_elec", *args, **kwargs)
