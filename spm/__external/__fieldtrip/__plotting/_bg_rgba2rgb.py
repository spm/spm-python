from spm.__wrapper__ import Runtime


def _bg_rgba2rgb(*args, **kwargs):
    """
      BG_RGBA2RGB overlays a transparency masked colored image on a colored background,  
        and represents the result as an RGB matrix.  
         
        Use as:  
          rgb = bg_rgba2rgb(bg, rgba)  
         
        or  
          rgb = bg_rgba2rgb(bg, rgba, cmap, clim, alpha, amap, alim);  
         
        When 2 input arguments are supplied:  
          bg   = Nx3 matrix of background rgb-coded color-values, or MxNx3  
          rgba = Nx4 matrix of rgb + alpha values, or MxNx4  
         
        When 7 input arguments are supplied:  
          bg   = Nx3 matrix, Nx1 vector, 1x3 vector, MxN, or MxNx3.  
          rgba = Nx1 vector with 'functional values', or MxN.  
          cmap = Mx3 colormap, or MATLAB-supported name of colormap  
          clim = 1x2 vector denoting the color limits  
          alpha = Nx1 vector with 'alpha values', or MxN  
          amap = Mx1 alphamap, or MATLAB -supported name of alphamap ('rampup/down', 'vup/down')  
          alim = 1x2 vector denoting the opacity limits  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/bg_rgba2rgb.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bg_rgba2rgb", *args, **kwargs)
