from spm.__wrap__ import _Runtime


def spm_dartel_import(*args, **kwargs):
  """  Import subjects' data for use with Dartel  
    FORMAT spm_dartel_import(job)  
    job.matnames  - Names of *_seg_sn.mat files to use  
    job.odir      - Output directory  
    job.bb        - Bounding box  
    job.vox       - Voxel sizes  
    job.GM/WM/CSF - Options fo different tissue classes  
    job.image     - Options for resliced original image  
     
    Rigidly aligned images are generated using info from the seg_sn.mat  
    files.  These can be resliced GM, WM or CSF, but also various resliced  
    forms of the original image (skull-stripped, bias corrected etc).  
   ___________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DARTEL/spm_dartel_import.m)
  """

  return _Runtime.call("spm_dartel_import", *args, **kwargs)
