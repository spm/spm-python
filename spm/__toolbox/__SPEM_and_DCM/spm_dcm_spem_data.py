from spm.__wrap__ import _Runtime


def spm_dcm_spem_data(*args, **kwargs):
  """  Prepare (decimate and normalise) data DCM for SPEM  
    FORMAT xY = spm_dcm_spem_data(xY)  
     
      xY.Y{i}  - original data  
      xY.C{i}  - original target  
      xY.DT    - original timing  
     
    creates:  
     
      xY.y{i} - normalised (decimated) lag (data - target)  
      xY.u{i} - normalised (decimated) target  
      xY.R(i) - decimation  
      xY.x(i) - intial states  
      xY.dt   - mean normalised (decimated) timing  
     
     This auxiliary routine  decimates and normalises eye movement data to a  
     single period of a (negative) cosine wave - of unit amplitude.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/SPEM_and_DCM/spm_dcm_spem_data.m)
  """

  return _Runtime.call("spm_dcm_spem_data", *args, **kwargs)
