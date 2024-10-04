from spm.__wrap__ import _Runtime


def spm_project(*args, **kwargs):
  """  Form maximum intensity projections - a compiled routine  
    FORMAT SPM = spm_project(X,L,dims,[DXYZ,CXYZ])  
    X      -   a matrix of voxel values  
    L      -   a matrix of locations  
    dims   -   assorted dimensions.  
                  dims(1:3) - the sizes of the projected rectangles.  
                  dims(4:5) - the dimensions of the mip image.  
    Optional:  
    DXYZ   - length of the X,Y,Z axes of the mip sections (in mip pixels).  
    CXYZ   - offsets of the origin into the mip sections (in mip pixels).  
   __________________________________________________________________________  
     
    spm_project 'fills in' a matrix (SPM) to create a maximum intensity  
    projection according to a point list of voxel values (V) and their  
    locations (L) in the standard space described in the atlas of Talairach &  
    Tournoux (1988) or another space defined by a customised mip template.  
     
    See also: spm_mip.m and spm_mip_ui.m  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_project.m)
  """

  return _Runtime.call("spm_project", *args, **kwargs)
