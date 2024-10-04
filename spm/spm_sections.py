from spm.__wrap__ import _Runtime


def spm_sections(*args, **kwargs):
  """  Rendering of regional effects [SPM{.}] on orthogonal sections  
    FORMAT spm_sections(xSPM,hReg,img)  
     
    xSPM  - structure containing details of excursion set (see spm_getSPM)  
    hReg  - handle of MIP register  
    img   - filename of background image  
   __________________________________________________________________________  
     
    spm_sections is called by spm_results_ui and uses variable img to  
    create three orthogonal sections through a background image.  
    Regional foci from the selected xSPM are rendered on this image.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_sections.m)
  """

  return _Runtime.call("spm_sections", *args, **kwargs, nargout=0)
