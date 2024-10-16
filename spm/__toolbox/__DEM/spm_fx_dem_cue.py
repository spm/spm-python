from spm.__wrapper__ import Runtime


def spm_fx_dem_cue(*args, **kwargs):
  """  returns the flow for cued response  
    FORMAT [f]= spm_fx_dem_cue(x,v,P)  
     
    x    - hidden states:  
      x.o  - intrinsic motor state (proprioceptive)  
      x.a  - target salience (attractiveness)  
     
    v    - hidden causes  
     
    P.x  - target locations (visual) - extrinsic coordinates (Cartesian)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_fx_dem_cue.m)
  """

  return Runtime.call("spm_fx_dem_cue", *args, **kwargs)
