from spm.__wrapper__ import Runtime


def uimagesc(*args, **kwargs):
    """
     UIMAGESC  Display scaled image with uneven axis.  
          UIMAGESC(...) is the same as UIMAGE(...) except the data is scaled  
          to use the full colormap. See UIMAGE for details.  
         
          Note: UIMAGESC is based on Matlab's original IMAGESC, Revision 5.11.4.5.  
          UIMAGESC simply calls UIMAGE with a scaled colormap.  
          
          F. Moisy - adapted from TMW  
          Revision: 1.01,  Date: 2006/06/13.  
         
          See also IMAGE, IMAGESC, UIMAGE.  
         
        This function is downloaded on Oct 24th 2008 from www.mathworks.com/matlabcentral/fileexchange/11368  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/external/fileexchange/uimagesc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("uimagesc", *args, **kwargs)
