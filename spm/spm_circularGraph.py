from spm.__wrapper__ import Runtime


def spm_circularGraph(*args, **kwargs):
    """
      Plot a circular graph to illustrate connections  
        FORMAT spm_circularGraph(A,'PropertyName',propertyvalue,...)  
        X      - symmetric (NxN) matrix of numeric or logical values  
         
        Optional properties:  
          'Colormap'     - (Nx3) matrix of [r g b] triples  
          'Label'        - cell array of N strings  
         
        A 'circular graph' is a visualization of a network of nodes and their  
        connections. The nodes are laid out along a circle, and the connections  
        are drawn within the circle.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_circularGraph.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_circularGraph", *args, **kwargs, nargout=0)
