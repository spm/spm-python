from spm.__wrap__ import _Runtime


def spm_glass(*args, **kwargs):
  """  Glass brain plot  
    FORMAT fig = spm_glass(X,pos,S)  
      X               - (REQUIRED) values to be painted  
      pos             - (REQUIRED) coordinates in MNI head (not voxel) space  
      S               - (optional) config structure  
    Fields of S:  
      S.brush         - brush size                   - Default: 0  
      S.cmap          - colormap of plot             - Default: 'gray'  
      S.dark          - dark mode                    - Default: false  
      S.detail        - glass brain detail level:  
                        0=LOW, 1=NORMAL, 2=HIGH      - Default: 1  
      S.grid          - overlay grid                 - Default: false  
      S.colourbar     - add colourbar                - Default: false  
      S.invertcolour  - flip the colourmap           - Default: false  
      S.dp            - decimal places for colourbar - Default: 1  
      S.fontname      - font for colourbar           - Default: Helvetica  
    Output:  
      fig             - Handle for generated figure  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_glass.m)
  """

  return _Runtime.call("spm_glass", *args, **kwargs)
