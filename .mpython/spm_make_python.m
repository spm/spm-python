function spm_make_python(workpath, compile, wrap)
try 
    cpath = workpath; 
catch
    [cpath, ~, ~] = fileparts(mfilename('fullpath'));
end
try
    compile = logical(compile); 
catch
    compile = true;
end
try 
    wrap = logical(wrap); 
catch 
    wrap = true; 
end

cd(cpath);

try 
    mkdir('external')
end
cd('external'); 

if ~exist('spm', 'dir')
    system('git clone --depth=1 https://github.com/spm/spm.git');
else 
    system('git -C spm pull');
end

if ~exist('mpython', 'dir')
    system('git clone --depth=1 https://github.com/MPython-Package-Factory/mpython.git');
else 
    system('git -C mpython pull');
end

cd('..'); 

try
    rmdir('build');
end
mkdir('build')

spmpath = fullfile(cpath, 'build', 'spm');
copyfile(fullfile('external', 'spm'), spmpath, 'f'); 

restoredefaultpath
addpath(fullfile('external', 'mpython'), spmpath); 
spm('defaults', 'eeg'); 
spm_jobman('initcfg')

copyfile(fullfile(spm('Dir'),'Contents.m'),...
         fullfile(spm('Dir'),'Contents.txt'));

ignored = {...
    '.git', ...
    '.github', ...
    'external/fieldtrip/compat/*', ...
    'external/fieldtrip/.git', ...
    'external/fieldtrip/.github',...
    'toolbox/DEM/VOX.mat',...
    'toolbox/DEM/DEM_lorenz_suprise.mat',...
    'toolbox/DEM/DEM_IMG.mat',...
    'toolbox/DEM/ADEM_saccades.mat',...
};
for d = ignored
    try 
        rmdir(fullfile(spmpath, d{1}), 's'); 
    end
    try 
        delete(fullfile(spmpath, d{1}));
    end
end

%==========================================================================
%-Static listing of SPM toolboxes
%==========================================================================
fid = fopen(fullfile(spm('Dir'),'config','spm_cfg_static_tools.m'),'wt');
fprintf(fid,'function values = spm_cfg_static_tools\n');
fprintf(fid,...
    '%% Static listing of all batch configuration files in the SPM toolbox folder\n');
%-Get the list of toolbox directories
tbxdir = fullfile(spm('Dir'),'toolbox');
d = [tbxdir; cellstr(spm_select('FPList',tbxdir,'dir'))];
ft = {};
%-Look for '*_cfg_*.m' files in these directories
for i=1:numel(d)
    fi = spm_select('List',d{i},'.*_cfg_.*\.m$');
    if ~isempty(fi)
        ft = [ft(:); cellstr(fi)];
    end
end
%-Create code to insert toolbox config
if isempty(ft)
    ftstr = '';
else
    ft = spm_file(ft,'basename');
    ftstr = sprintf('%s ', ft{:});
end
fprintf(fid,'values = {%s};\n', ftstr);
fclose(fid);

%==========================================================================
%-Static listing of batch application initialisation files
%==========================================================================
cfg_util('dumpcfg');

toolboxes = {
    'parfor', ...
    'stats', ...
    'images',...
    'signal'...
};


opath = fullfile(cpath, '..');

if compile
    mpython_compile(spmpath, opath, 'spm', toolboxes)
end

if wrap
    mpython_wrap(spmpath, opath, 'spm', true, fullfile(cpath, 'templates'))
end

disp('Done!');
