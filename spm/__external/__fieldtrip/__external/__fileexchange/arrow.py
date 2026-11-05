from spm._runtime import Runtime


def arrow(*args, **kwargs):
    r"""
      ARROW  Draw a line with an arrowhead.  
         
         ARROW(Start,Stop) draws a line with an arrow from Start to Stop (points  
               should be vectors of length 2 or 3, or matrices with 2 or 3  
               columns), and returns the graphics handle of the arrow(s).  
         
         ARROW uses the mouse (click-drag) to create an arrow.  
         
         ARROW DEMO & ARROW DEMO2 show 3-D & 2-D demos of the capabilities of ARROW.  
         
         ARROW may be called with a normal argument list or a property-based list.  
               ARROW(Start,Stop,Length,BaseAngle,TipAngle,Width,Page,CrossDir) is  
               the full normal argument list, where all but the Start and Stop  
               points are optional.  If you need to specify a later argument (e.g.,  
               Page) but want default values of earlier ones (e.g., TipAngle),  
               pass an empty matrix for the earlier ones (e.g., TipAngle=[]).  
         
         ARROW('Property1',PropVal1,'Property2',PropVal2,...) creates arrows with the  
               given properties, using default values for any unspecified or given as  
               'default' or NaN.  Some properties used for line and patch objects are  
               used in a modified fashion, others are passed directly to LINE, PATCH,  
               or SET.  For a detailed properties explanation, call ARROW PROPERTIES.  
         
               Start         The starting points.                     B  
               Stop          The end points.                         /|\           ^  
               Length        Length of the arrowhead in pixels.     /|||\          |  
               BaseAngle     Base angle in degrees (ADE).          //|||\\        L|  
               TipAngle      Tip angle in degrees (ABC).          ///|||\\\       e|  
               Width         Width of the base in pixels.        ////|||\\\\      n|  
               Page          Use hardcopy proportions.          /////|D|\\\\\     g|  
               CrossDir      Vector || to arrowhead plane.     ////  |||  \\\\    t|  
               NormalDir     Vector out of arrowhead plane.   ///    |||    \\\   h|  
               Ends          Which end has an arrowhead.     //<----->||      \\   |  
               ObjectHandles Vector of handles to update.   /   base |||        \  V  
                                                           E    angle||<-------->C  
         ARROW(H,'Prop1',PropVal1,...), where H is a                 |||tipangle  
               vector of handles to previously-created arrows        |||  
               and/or line objects, will update the previously-      |||  
               created arrows according to the current view       -->|A|<-- width  
               and any specified properties, and will convert  
               two-point line objects to corresponding arrows.  ARROW(H) will update  
               the arrows if the current view has changed.  Root, figure, or axes  
               handles included in H are replaced by all descendant Arrow objects.  
         
         A property list can follow any specified normal argument list, e.g.,  
         ARROW([1 2 3],[0 0 0],36,'BaseAngle',60) creates an arrow from (1,2,3) to  
         the origin, with an arrowhead of length 36 pixels and 60-degree base angle.  
         
         The basic arguments or properties can generally be vectorized to create  
         multiple arrows with the same call.  This is done by passing a property  
         with one row per arrow, or, if all arrows are to have the same property  
         value, just one row may be specified.  
         
         You may want to execute AXIS(AXIS) before calling ARROW so it doesn't change  
         the axes on you; ARROW determines the sizes of arrow components BEFORE the  
         arrow is plotted, so if ARROW changes axis limits, arrows may be malformed.  
         
         This version of ARROW uses features of MATLAB 5 and is incompatible with  
         earlier MATLAB versions (ARROW for MATLAB 4.2c is available separately);  
         some problems with perspective plots still exist.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/fileexchange/arrow.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("arrow", *args, **kwargs)
