from spm.__wrapper__ import Runtime


def spm_colourmap(*args, **kwargs):
    """
      Colourmap multi-function  
        FORMAT map = spm_colourmap  
        Return the colourmap of the current figure as a three-column matrix of  
        RGB triplets (between 0.0 and 1.0).  
         
        FORMAT [map =] spm_colourmap(map)  
        Define a colourmap or set it to the current figure.  
        map         - gray, hot, pink, jet, ...: built-in colourmaps {64 x 3}  
                    - gray-hot, ...: creates a 'split' colourmap {128 x 3 matrix}  
                      The lower half is a gray scale and the upper half is  
                      selected colourmap. This colourmap is used for viewing  
                      'rendered' SPMs on a PET, MRI or other background images.  
          
        FORMAT [map = ] spm_colourmap(effect[,map])  
        Apply an effect to a colourmap then return it or apply it to the current  
        figure.  
        effect      - 'Invert'   - invert (flip) the colourmap  
                      'Brighten' - call MATLAB's brighten with a beta of +0.2  
                      'Darken'   - call MATLAB's brighten with a beta of -0.2  
         
        FORMAT maps = spm_colourmap('list')  
        Return the list of all colourmaps' name (see graph3d).  
         
        FORMAT [map =] spm_colourmap('load',fname)  
        Load a colourmap from file (*.lut, *.cmap, *.mat) then return it or apply  
        it to the current figure.  
         
        FORMAT spm_colourmap('save',fname[,map])  
        Save a colourmap to file (format according to file extension).  
       __________________________________________________________________________  
         
        A repository of colourmaps with linearised luminance is available at:  
          https://github.com/CPernet/brain_colours  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_colourmap.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_colourmap", *args, **kwargs)
