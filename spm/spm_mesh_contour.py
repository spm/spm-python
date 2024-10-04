from spm.__wrap__ import _Runtime


def spm_mesh_contour(*args, **kwargs):
  """  Compute contour lines of a triangular mesh  
    FORMAT S = spm_mesh_contour(M,z)  
    M   - a GIfTI object or patch structure  
    z   - height of z-plane  
     
    FORMAT S = spm_mesh_contour(M,mat)  
    mat - 4 x 4 transformation matrix  
          (use z-plane at z = 0 after linear transformation according to mat)  
     
    S   - struct array of contour lines with fields 'xdata', 'ydata',  
          'zdata' and 'isopen'  
   __________________________________________________________________________  
     
    figure, hold on, axis equal  
    M = gifti(fullfile(spm('Dir'),'canonical','cortex_20484.surf.gii'));  
    z = linspace(min(M.vertices(:,3)),max(M.vertices(:,3)),20);  
    for i=1:numel(z)  
      S = spm_mesh_contour(M,z(i));  
      for j=1:numel(S)  
        plot3(S(j).xdata,S(j).ydata,S(j).zdata);  
      end  
    end  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mesh_contour.m)
  """

  return _Runtime.call("spm_mesh_contour", *args, **kwargs)
