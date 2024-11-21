from spm.__wrapper__ import Runtime


def _select3d(*args, **kwargs):
    """
     SELECT3D(H) Determines the selected point in 3-D data space.  
         P = SELECT3D determines the point, P, in data space corresponding   
         to the current selection position. P is a point on the first   
         patch or surface face intersected along the selection ray. If no   
         face is encountered along the selection ray, P returns empty.  
         
         P = SELECT3D(H) constrains selection to graphics handle H and,  
         if applicable, any of its children. H can be a figure, axes,   
         patch, or surface object.  
         
         [P V] = SELECT3D(...), V is the closest face or line vertex   
         selected based on the figure's current object.   
         
         [P V VI] = SELECT3D(...), VI is the index into the object's   
         x,y,zdata properties corresponding to V, the closest face vertex   
         selected.  
         
         [P V VI FACEV] = SELECT3D(...), FACE is an array of vertices   
         corresponding to the face polygon containing P and V.   
           
         [P V VI FACEV FACEI] = SELECT3D(...), FACEI is the row index into   
         the object's face array corresponding to FACE. For patch   
         objects, the face array can be obtained by doing   
         get(mypatch,'faces'). For surface objects, the face array   
         can be obtained from the output of SURF2PATCH (see   
         SURF2PATCH for more information).  
         
         RESTRICTIONS:  
         SELECT3D supports surface, patch, or line object primitives. For surface   
         and patches, the algorithm assumes non-self-intersecting planar faces.   
         For line objects, the algorithm always returns P as empty, and V will  
         be the closest vertex relative to the selection point.   
         
         Example:  
         
         h = surf(peaks);  
         zoom(10);  
         disp('Click anywhere on the surface, then hit return')  
         pause  
         [p v vi face facei] = select3d;  
         marker1 = line('xdata',p(1),'ydata',p(2),'zdata',p(3),'marker','o',...  
                        'erasemode','xor','markerfacecolor','k');  
         marker2 = line('xdata',v(1),'ydata',v(2),'zdata',v(3),'marker','o',...  
                        'erasemode','xor','markerfacecolor','k');  
         marker2 = line('erasemode','xor','xdata',face(1,:),'ydata',face(2,:),...  
                        'zdata',face(3,:),'linewidth',10);  
         disp(sprintf('\nYou clicked at\nX: %.2f\nY: %.2f\nZ: %.2f',p(1),p(2),p(3)'))  
         disp(sprintf('\nThe nearest vertex is\nX: %.2f\nY: %.2f\nZ: %.2f',v(1),v(2),v(3)'))  
          
         Version 1.2 2-15-02  
         Copyright Joe Conti 2002   
         Send comments to jconti@mathworks.com  
         
         See also GINPUT, GCO.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/select3d.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("select3d", *args, **kwargs)
