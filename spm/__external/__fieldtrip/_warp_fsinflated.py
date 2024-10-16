from spm.__wrapper__ import Runtime


def _warp_fsinflated(*args, **kwargs):
  """  WARP_FSINFLATED maps electrodes from FreeSurfer's pial surface to  
    FreeSurfer's inflated brain.  
     
    The configuration must contain the following options:  
      cfg.headshape      = string, filename containing subject headshape  
                         (e.g. <path to freesurfer/surf/lh.pial>)  
      cfg.fshome         = string, path to freesurfer  
     
    See also FT_ELECTRODEREALIGN, FT_PREPARE_MESH  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/warp_fsinflated.m)
  """

  return Runtime.call("warp_fsinflated", *args, **kwargs)
