from spm._runtime import Runtime


def breakout(*args, **kwargs):
    r"""
     BREAKOUT  Pong-like arcade game, a.k.a. Arkanoid/Brickles  
          Breakout begins with five rows of bricks, each row a different color.   
          The color order from the bottom up is blue, cyan, green, green and red.   
          Using a single ball, the player must knock down as many bricks as   
          possible by using the walls and/or the paddle below to ricochet the   
          ball against the bricks and eliminate them. Blue bricks earn one point   
          each, cyan bricks earn two points, green bricks earn three points,  
          yellow bricks earn four and the top-level red bricks score five points   
          each. To add to the challenge, the paddle shrinks to one-half its size   
          after the ball has broken through the red row and hit the upper wall.   
          (adapted from Wikipedia)  
         
          Game Controls:  
          Paddle is controlled with mouse.  
          Nine speed levels, changed using num-keys: 1...9.  
          Sound effects are switched on/off using 'S'.  
          Game is paused either with mouse press or 'P'.  
            
          Example:  
              breakout    % Start Main Breakout Interface  
          Developed by Per-Anders Ekstr�m, 2003-2007 Facilia AB.  
          New pointer control by Joseph Kirk (jdkirk630@gmail.com)  
         
         
        https://uk.mathworks.com/matlabcentral/fileexchange/14152-breakout  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/breakout.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("breakout", *args, **kwargs, nargout=0)
