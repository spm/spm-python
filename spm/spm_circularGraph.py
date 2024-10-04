from spm.__wrap__ import _Runtime


def spm_circularGraph(*args, **kwargs):
  """  Plot a circular graph to illustrate connections  
    FORMAT spm_circularGraph(A,'PropertyName',propertyvalue,...)  
    X      - symmetric (NxN) matrix of numeric or logical values  
     
    Optional properties:  
      'Colormap'     - (Nx3) matrix of [r g b] triples  
      'Label'        - cell array of N strings  
     
    A 'circular graph' is a visualization of a network of nodes and their  
    connections. The nodes are laid out along a circle, and the connections  
    are drawn within the circle.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_circularGraph.m)
  """

  return _Runtime.call("spm_circularGraph", *args, **kwargs, nargout=0)
