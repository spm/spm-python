from spm.__wrap__ import _Runtime


def spm_vb_set_priors(*args, **kwargs):
  """  Set up precision parameters and optimisation options to correspond to priors  
    FORMAT [block] = spm_vb_set_priors(block,priors,vxyz)  
     
    block   - VB-GLM-AR data structure (see spm_vb_glmar)  
    priors  - For regression coefficients:  
     
              .W= 'Spatial - UGL' : coeffs that are spatially regularised  
                  'Spatial - GMRF' : as above but different spatial prior  
                  'Spatial - LORETA' : as above but different spatial prior  
                  'Spatial - WGL' : as above but different spatial prior  
                  'Voxel - Shrinkage' : that are shrunk voxel-wise  
                  'Voxel - Uninformative' : coeffs without prior  
     
              For AR coefficients:  
     
              .A= 'Spatial - UGL' : coeffs that are spatially regularised  
                  'Spatial - GMRF' : as above but different spatial prior  
                  'Spatial - LORETA' : as above but different spatial prior  
                  'Voxel - Shrinkage' : that are shrunk voxel-wise  
                  'Voxel - Uninformative' : coeffs without prior  
                  'Voxel - Limiting' : Voxel-specific coeffs as limiting case  
                                       of a LORETA prior  
                  'block - Limiting' : block-specific coeffs as limiting case  
                                       of a LORETA prior  
                  'Discrete' : Different coeffs as function of grey/white/CSF  
                               or other masks  
     
    vxyz    - locations of voxels   
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_vb_set_priors.m)
  """

  return _Runtime.call("spm_vb_set_priors", *args, **kwargs)
