from spm.__wrapper__ import Runtime


def spm_vb_spatial_precision(*args, **kwargs):
  """  Compute spatial precision matrix appropriate to prior  
    FORMAT [S] = spm_vb_spatial_precision(prior_type,vxyz,img)  
     
    prior_type - type of prior {'Spatial - UGL','Spatial - GMRF',...  
                                'Spatial - LORETA','Spatial - WGL'}  
    vxyz       - list of voxels  
    img        - used to construct weights of WGL  
     
    S          - spatial precision matrix  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_vb_spatial_precision.m)
  """

  return Runtime.call("spm_vb_spatial_precision", *args, **kwargs)
