from spm.__wrapper__ import Runtime


def _htmlcolors(*args, **kwargs):
    """
      HTMLCOLORS looks up the RGB value for a named color (string), or the name for a given RGB value  
         
        Use as  
          rgb = htmlcolors(name)  
        or  
          name = htmlcolors(rgb)  
        or   
          list = htmlcolors  
         
        See https://www.rapidtables.com/web/color/html-color-codes.html  
        and https://www.color-hex.com/color-palettes/  
         
        See also FT_COLORMAP, COLORMAP, COLORMAPEDITOR, BREWERMAP, MATPLOTLIB, CMOCEAN  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/htmlcolors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("htmlcolors", *args, **kwargs)
