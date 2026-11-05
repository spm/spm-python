from spm._runtime import Runtime


def subtightplot(*args, **kwargs):
    r"""
     function h=subtightplot(m,n,p,gap,marg_h,marg_w,varargin)  
         
        Functional purpose: A wrapper function for Matlab function subplot. Adds the ability to define the gap between  
        neighbouring subplots. Unfotrtunately Matlab subplot function lacks this functionality, and the gap between  
        subplots can reach 40% of figure area, which is pretty lavish.    
         
        Input arguments (defaults exist):  
          gap- two elements vector [vertical,horizontal] defining the gap between neighbouring axes. Default value  
                   is 0.01. Note this vale will cause titles legends and labels to collide with the subplots, while presenting  
                   relatively large axis.   
          marg_h  margins in height in normalized units (0...1)  
                   or [lower uppper] for different lower and upper margins   
          marg_w  margins in width in normalized units (0...1)  
                   or [left right] for different left and right margins   
         
        Output arguments: same as subplot- none, or axes handle according to function call.  
         
        Issues & Comments: Note that if additional elements are used in order to be passed to subplot, gap parameter must  
              be defined. For default gap value use empty element- [].        
         
        Usage example: h=subtightplot((2,3,1:2,[0.5,0.2])  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/fileexchange/subtightplot.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("subtightplot", *args, **kwargs)
