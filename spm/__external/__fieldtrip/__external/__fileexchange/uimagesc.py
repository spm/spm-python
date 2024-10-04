from spm.__wrap__ import _Runtime


def uimagesc(*args, **kwargs):
  """ UIMAGESC  Display scaled image with uneven axis.  
      UIMAGESC(...) is the same as UIMAGE(...) except the data is scaled  
      to use the full colormap. See UIMAGE for details.  
     
      Note: UIMAGESC is based on Matlab's original IMAGESC, Revision 5.11.4.5.  
      UIMAGESC simply calls UIMAGE with a scaled colormap.  
      
      F. Moisy - adapted from TMW  
      Revision: 1.01,  Date: 2006/06/13.  
     
      See also IMAGE, IMAGESC, UIMAGE.  
     
    This function is downloaded on Oct 24th 2008 from www.mathworks.com/matlabcentral/fileexchange/11368  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/external/fileexchange/uimagesc.m)
  """

  return _Runtime.call("uimagesc", *args, **kwargs)
