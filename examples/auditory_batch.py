"""
This batch script analyses the Auditory fMRI dataset available from the
SPM website:
  http://www.fil.ion.ucl.ac.uk/spm/data/auditory/
as described in the SPM manual:
  http://www.fil.ion.ucl.ac.uk/spm/doc/manual.pdf#Chap:data:auditory
________________________________________________________________________
Copyright (C) 2014 Wellcome Trust Centre for Neuroimaging

Matlab: Guillaume Flandin
Python: Yael Balbastre
"""

import zipfile
import os.path as op
import spm

num = spm.Array.from_any

# Directory containing the Auditory data
# ----------------------------------------------------------------------

url = "https://www.fil.ion.ucl.ac.uk/spm/download/data/MoAEpilot/MoAEpilot.zip"
data_path = op.dirname(__file__)
zip_path = op.join(data_path, "MoAEpilot.zip")

print(f"{'Downloading Auditory dataset...':<40s}")
spm.Runtime.call("urlwrite", url, zip_path)
with zipfile.ZipFile(zip_path, "r") as f:
    f.extractall(data_path)
print(f" {'...done':30s}\n")


# Initialise SPM
# ----------------------------------------------------------------------
spm.spm("Defaults", "fMRI")
spm.spm_jobman("initcfg", nargout=0)
# spm.spm_get_defaults('cmdline', true)

# ======================================================================
# PREAMBLE: DUMMY SCANS
# ======================================================================

f = spm.spm_select("FPList", op.join(data_path, "fM00223"), r"^f.*\.img$")

matlabbatch = spm.Cell()

matlabbatch(0).cfg_basicio.file_dir.dir_ops.cfg_mkdir.parent = [data_path]
matlabbatch(0).cfg_basicio.file_dir.dir_ops.cfg_mkdir.name = "dummy"

matlabbatch(0).cfg_basicio.file_dir.file_ops.file_move.files = f[:12]
matlabbatch(0).cfg_basicio.file_dir.file_ops.file_move.action.moveto = [
    op.join(data_path, "dummy")
]

spm.spm_jobman("run", matlabbatch, nargout=0)

# ======================================================================
# SPATIAL PREPROCESSING
# ======================================================================

f = spm.spm_select("FPList", op.join(data_path, "fM00223"), r"^f.*\.img$")
a = spm.spm_select("FPList", op.join(data_path, "sM00223"), r"^s.*\.img$")

matlabbatch = spm.Cell()

# Realign
# ----------------------------------------------------------------------
matlabbatch(0).spm.spatial.realign.estwrite.data = [f]
matlabbatch(0).spm.spatial.realign.estwrite.roptions.which = num([0, 1])

# Coregister
# ----------------------------------------------------------------------
matlabbatch(1).spm.spatial.coreg.estimate.ref = [
    spm.spm_file(f[0, 0], "prefix", "mean")
]
matlabbatch(1).spm.spatial.coreg.estimate.source = [a]

# Segment
# ----------------------------------------------------------------------
matlabbatch(2).spm.spatial.preproc.channel.vols = [a]
matlabbatch(2).spm.spatial.preproc.channel.write = num([0, 1])
matlabbatch(2).spm.spatial.preproc.warp.write = num([0, 1])

# Normalise: Write
# ----------------------------------------------------------------------
matlabbatch(3).spm.spatial.normalise.write.subj["def"] = [
    spm.spm_file(a, "prefix", "y_", "ext", "nii")
]
matlabbatch(3).spm.spatial.normalise.write.subj.resample = f
matlabbatch(3).spm.spatial.normalise.write.woptions.vox = num([3, 3, 3])

matlabbatch(4).spm.spatial.normalise.write.subj["def"] = [
    spm.spm_file(a, "prefix", "y_", "ext", "nii")
]
matlabbatch(4).spm.spatial.normalise.write.subj.resample = [
    spm.spm_file(a, "prefix", "m", "ext", "nii")
]
matlabbatch(4).spm.spatial.normalise.write.woptions.vox = num([1, 1, 3])

# Smooth
# ----------------------------------------------------------------------
matlabbatch(5).spm.spatial.smooth.data = spm.spm_file(f, "prefix", "w")[:, None]
matlabbatch(5).spm.spatial.smooth.fwhm = num([6, 6, 6])

spm.spm_jobman("run", matlabbatch, nargout=0)

# ======================================================================
# GLM SPECIFICATION, ESTIMATION, INFERENCE, RESULTS
# ======================================================================

f = spm.spm_select("FPList", op.join(data_path, "fM00223"), r"^swf.*\.img$")

matlabbatch = spm.Cell()

# Output Directory
# ----------------------------------------------------------------------
matlabbatch(0).cfg_basicio.file_dir.dir_ops.cfg_mkdir.parent = [data_path]
matlabbatch(0).cfg_basicio.file_dir.dir_ops.cfg_mkdir.name = "GLM"

# Model Specification
# ----------------------------------------------------------------------
matlabbatch(1).spm.stats.fmri_spec.dir = [op.join(data_path, "GLM")]
matlabbatch(1).spm.stats.fmri_spec.timing.units = "scans"
matlabbatch(1).spm.stats.fmri_spec.timing.RT = 7
matlabbatch(1).spm.stats.fmri_spec.sess.scans = f
matlabbatch(1).spm.stats.fmri_spec.sess.cond.name = "active"
matlabbatch(1).spm.stats.fmri_spec.sess.cond.onset = num(range(6, 86, 12))
matlabbatch(1).spm.stats.fmri_spec.sess.cond.duration = 6

# Model Estimation
# ----------------------------------------------------------------------
matlabbatch(2).spm.stats.fmri_est.spmmat = [op.join(data_path, "GLM", "SPM.mat")]

# Contrasts
# ----------------------------------------------------------------------
matlabbatch(3).spm.stats.con.spmmat = [op.join(data_path, "GLM", "SPM.mat")]
matlabbatch(3).spm.stats.con.consess(0).tcon.name = "Listening > Rest"
matlabbatch(3).spm.stats.con.consess(0).tcon.weights = num([1, 0])
matlabbatch(3).spm.stats.con.consess(1).tcon.name = "Rest > Listening"
matlabbatch(3).spm.stats.con.consess(1).tcon.weights = num([-1, 0])

# Inference Results
# ----------------------------------------------------------------------
matlabbatch(4).spm.stats.results.spmmat = [op.join(data_path, "GLM", "SPM.mat")]
matlabbatch(4).spm.stats.results.conspec.contrasts = 1
matlabbatch(4).spm.stats.results.conspec.threshdesc = "FWE"
matlabbatch(4).spm.stats.results.conspec.thresh = 0.05
matlabbatch(4).spm.stats.results.conspec.extent = 0
matlabbatch(4).spm.stats.results.print = False

# Rendering
# ----------------------------------------------------------------------
matlabbatch(5).spm.util.render.display.rendfile = [
    op.join(spm.spm("Dir"), "canonical", "cortex_20484.surf.gii")
]
matlabbatch(5).spm.util.render.display.conspec.spmmat = [
    op.join(data_path, "GLM", "SPM.mat")
]
matlabbatch(5).spm.util.render.display.conspec.contrasts = 1
matlabbatch(5).spm.util.render.display.conspec.threshdesc = "FWE"
matlabbatch(5).spm.util.render.display.conspec.thresh = 0.05
matlabbatch(5).spm.util.render.display.conspec.extent = 0

spm.spm_jobman("run", matlabbatch, nargout=0)
