from spm.__wrapper__ import Runtime


def uimage(*args, **kwargs):
    """
     UIMAGE  Display image with uneven axis.  
          UIMAGE(X,Y,C) displays matrix C as an image, using the vectors X and  
          Y to specify the X and Y coordinates. X and Y may be unevenly spaced  
          vectors, but must be increasing. The size of C must be LENGTH(Y)*  
          LENGTH(X). (Most probably you'll want to display C' instead of C).  
         
          Contrary to Matlab's original IMAGE function, here the vectors X and Y  
          do not need to be linearly spaced. Whereas IMAGE linearly interpolates  
          the X-axis between X(1) and X(end), ignoring all other values (idem  
          for Y), UIMAGE allows for X and/or Y to be unevenly spaced vectors, by  
          locally stretching the matrix C (ie, by duplicating some elements of C)  
          for larger X and/or Y intervals.  
         
          The syntax for UIMAGE(X,Y,C,...) is the same as IMAGE(X,Y,C,...)  
          (all the remaining arguments, eg 'PropertyName'-PropertyValue pairs,  
          are passed to IMAGE). See IMAGE for details.  
         
          Use UIMAGESC to scale the data using the full colormap. The syntax for  
          UIMAGESC(X,Y,C,...) is the same as IMAGESC(X,Y,C,...).  
         
          Typical uses:  
             - Plotting a spatio-temporal diagram (T,X), with unevenly spaced  
             time intervals for T (eg, when some values are missing, or when  
             using a non-constant sampling rate).  
             - Plotting a set of power spectra with frequency in log-scale.  
         
          h = UIMAGE(X,Y,C,...) returns a handle to the image.  
         
          Example:  
            c = randn(50,20);         % Random 50x20 matrix  
            x = logspace(1,3,50);     % log-spaced X-axis, between 10 and 1000  
            y = linspace(3,8,20);     % lin-spaced Y-axis, between 3 and 8  
            uimagesc(x,y,c');         % displays the matrix  
         
          F. Moisy  
          Revision: 1.03,  Date: 2006/06/14.  
         
          See also IMAGE, IMAGESC, UIMAGESC.  
         
        This function is downloaded on Oct 24th 2008 from www.mathworks.com/matlabcentral/fileexchange/11368  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/external/fileexchange/uimage.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("uimage", *args, **kwargs)
