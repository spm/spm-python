from spm.__wrapper__ import Runtime


def ft_colormap(*args, **kwargs):
    """
      FT_COLORMAP is a wrapper function with the same usage as the normal COLORMAP  
        function, but it also knows about the colormaps from BREWERMAP and some colormaps  
        from MATPLOTLIB. The recommended colormaps include 'parula', 'cividis', 'balance',  
        and '*RdBu'.  
         
        Use as  
          ft_colormap(name)  
          ft_colormap(name, n)  
          ft_colormap(handle, name)  
          ft_colormap(handle, name, n)  
         
        The name is a string that specifies the colormap (see below). The optional handle  
        can be used to specify the current figure (which is the default, see GCF) or the  
        current axes (see GCA). The optional parameter n determines the number of steps or  
        unique colors in the map (by default 64).  
         
        The colormaps from MATLAB include 'parula', 'jet', 'hsv', 'hot', 'cool', 'spring',  
        'summer', 'autumn', 'winter', 'gray', 'bone', 'copper', 'pink', 'lines',  
        'colorcube', 'prism', and 'flag'.  
         
        The colormaps from MATPLOTLIB include 'cividis', 'inferno', 'magma', 'plasma',  
        'tab10', 'tab20', 'tab20b', 'tab20c', 'twilight', and 'viridis'.  
         
        The colormaps from BREWERMAP include 'BrBG', 'PRGn', 'PiYG', 'PuOr', 'RdBu',  
        'RdGy', 'RdYlBu', 'RdYlGn', 'Spectral', 'Accent', 'Dark2', 'Paired', 'Pastel1',  
        'Pastel2', 'Set1', 'Set2', 'Set3', 'Blues', 'BuGn', 'BuPu', 'GnBu', 'Greens',  
        'Greys', 'OrRd', 'Oranges', 'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu', 'Reds',  
        'YlGn', 'YlGnBu', 'YlOrBr', and 'YlOrRd', plus their reverse when prefixed with '*'.  
         
        The colormaps from CMOCEAN include 'thermal', 'haline', 'solar', 'ice', 'gray',  
        'oxy', 'deep', 'dense', 'algae', 'matter', 'turbid', 'speed', 'amp', 'tempo',  
        'rain', 'phase', 'topo', 'balance', 'delta', 'curl', 'diff', and 'tarn'.  
         
        The colormaps from COLORCET include 'blueternary', 'coolwarm', 'cyclicgrey',  
        'depth', 'divbjy', 'fire', 'geographic', 'geographic2', 'gouldian', 'gray',  
        'greenternary', 'grey', 'heat', 'phase2', 'phase4', 'rainbow', 'rainbow2',  
        'rainbow3', 'rainbow4', 'redternary', 'reducedgrey', 'yellowheat', and all the ones  
        with symbolic names.  
         
        To reverse any of these these colormaps you can add a minus sign in front, like  
        '-phase', '-balance' or '-RdBu'.  
         
        Relevant publications:  
        - Crameri et al. 2020. The misuse of colour in science communication. https://doi.org/10.1038/s41467-020-19160-7  
        - Cooper et al. 2021. Over the rainbow: Guidelines for meaningful use of colour maps in neurophysiology. https://doi.org/10.1016/j.neuroimage.2021.118628  
        - Kovesi 2015, Good colour maps: How to design them. https://doi.org/10.48550/arXiv.1509.03700  
         
        See also COLORMAP, COLORMAPEDITOR, BREWERMAP, MATPLOTLIB, CMOCEAN, COLORCET  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/ft_colormap.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_colormap", *args, **kwargs)
