from spm._runtime import Runtime


def spm_circularGraph(*args, **kwargs):
    r"""
      Plot a circular graph to illustrate connections  
        FORMAT spm_circularGraph(A,'PropertyName',propertyvalue,...)  
        X      - symmetric (NxN) matrix of numeric or logical values  
         
        Optional properties:  
          'Colormap'     - (Nx3) matrix of [r g b] triples  
          'Label'        - cell array of N strings  
         
        A 'circular graph' is a visualization of a network of nodes and their  
        connections. The nodes are laid out along a circle, and the connections  
        are drawn within the circle.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_circularGraph.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_circularGraph", *args, **kwargs, nargout=0)
